from datetime import datetime
from django.conf import settings
import gevent
from gevent.event import Event
from gevent.lock import RLock
import glob
import os
from os.path import abspath, exists, join
import re
import time
import signal
import logging
import subprocess
from tempfile import mkstemp
from threading import current_thread

from simulationAPI.helpers import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blocks.settings')

SCILAB_DIR = abspath(settings.SCILAB_DIR)
SCILAB = join(SCILAB_DIR, 'bin', 'scilab-adv-cli')
BASEDIR = abspath('src/static')
IMAGEDIR = join(BASEDIR, config.IMAGEDIR)


SESSIONDIR = abspath(config.SESSIONDIR)

VALUES_FOLDER = 'values'  # to store files related to tkscale block

# Delay time to look for new line (in s)
LOOK_DELAY = 0.1

SCILAB_START = (
    "try;funcprot(0);lines(0,120);"
    "clearfun('messagebox');"
    "function messagebox(msg,title,icon,buttons,modal),disp(msg),endfunction;"
    "funcprot(1);"
    "catch;[error_message,error_number,error_line,error_func]=lasterror();"
    "disp(error_message,error_number,error_line,error_func);exit(3);end;"
)
SCILAB_END = (
    "catch;[error_message,error_number,error_line,error_func]=lasterror();"
    "disp(error_message,error_number,error_line,error_func);exit(2);end;exit;"
)

SCILAB_CMD = [SCILAB,
              "-noatomsautoload",
              "-nogui",
              "-nouserstartup",
              "-nb",
              "-nw",
              "-e", SCILAB_START]

USER_DATA = {}


def makedirs(dirname, dirtype):
    if not exists(dirname):
        os.makedirs(dirname)


def remove(filename):
    if filename is None:
        return False
    if not config.REMOVEFILE:
        logger.debug('not removing %s', filename)
        return True
    try:
        os.remove(filename)
        return True
    except BaseException:
        logger.error('could not remove %s', filename)
        return False


# Configure logger
logger = logging.getLogger(__name__)  # Create a logger for this module
logger.setLevel(logging.INFO)  # Set logging level

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Define log message format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)

makedirs(SESSIONDIR, 'top session')


class ScilabInstance:
    proc = None
    log_name = None
    base = None
    starttime = None
    endtime = None

    def __init__(self):
        (self.proc, self.log_name) = prestart_scilab()

    def __str__(self):
        return "{pid: %s, log_name: %s}" % (self.proc.pid, self.log_name)


class Diagram:
    diagram_id = None
    # session dir
    sessiondir = None
    # store uploaded filename
    xcos_file_name = None
    # type of uploaded file
    workspace_counter = 0
    save_variables = set()
    # workspace from script
    workspace_filename = None
    # tk count
    tk_count = 0
    # store log name
    instance = None
    # is thread running?
    tkbool = False
    tk_starttime = None
    # in memory values
    tk_deltatimes = None
    tk_values = None
    tk_times = None
    # List to store figure IDs from log_name
    figure_list = None
    file_image = ''

    def __init__(self):
        self.figure_list = []

    def __str__(self):
        return "{instance: %s, tkbool: %s, figure_list: %s}" % (
            self.instance, self.tkbool, self.figure_list)

    def clean(self):
        if self.instance is not None:
            kill_scilab(self)
            self.instance = None
        if self.xcos_file_name is not None:
            remove(self.xcos_file_name)
            self.xcos_file_name = None
        if self.workspace_filename is not None:
            remove(self.workspace_filename)
            self.workspace_filename = None
        if self.file_image != '':
            remove(join(IMAGEDIR, self.file_image))
            self.file_image = ''


INSTANCES_1 = []
INSTANCES_2 = []
evt = Event()


def no_free_scilab_instance():
    l1 = len(INSTANCES_1)
    return l1 == 0


def too_many_scilab_instances():
    l1 = len(INSTANCES_1)
    l2 = len(INSTANCES_2)
    return l1 >= config.SCILAB_MIN_INSTANCES or \
        l1 + l2 >= config.SCILAB_MAX_INSTANCES


def start_scilab_instances():
    l1 = len(INSTANCES_1)
    l2 = len(INSTANCES_2)
    lssi = min(config.SCILAB_START_INSTANCES,
               config.SCILAB_MAX_INSTANCES - l2) - l1
    if lssi > 0:
        logger.info('can start %s instances', lssi)
    return lssi


def print_scilab_instances():
    l1 = len(INSTANCES_1)
    l2 = len(INSTANCES_2)
    msg = ''
    if l1 > 0:
        msg += ', free=' + str(l1)
    if l2 > 0:
        msg += ', in use=' + str(l2)
    logger.info('instance count: %s', msg[2:])


FIRST_INSTANCE = True


def prestart_scilab_instances():
    global FIRST_INSTANCE

    current_thread().name = 'PreStart'

    attempt = 1

    while True:
        while too_many_scilab_instances():
            evt.wait()

        for i in range(start_scilab_instances()):
            instance = ScilabInstance()
            proc = instance.proc
            if proc is None:
                gevent.thread.interrupt_main()
                return

            if FIRST_INSTANCE:
                gevent.sleep(1)
                for i in range(2, 4):
                    if proc.poll() is not None:
                        break
                    gevent.sleep(i)

            if proc.poll() is not None:
                (out, err) = proc.communicate()
                out = re.sub(r'^[ !\\-]*\n', r'', out, flags=re.MULTILINE)
                if out:
                    logger.info('=== Output from scilab console ===\n%s',
                                out)
                if err:
                    logger.info('=== Error from scilab console ===\n%s',
                                err)

                # Check for errors in Scilab
                if 'Cannot find scilab-bin' in out:
                    logger.critical('scilab has not been built. '
                                    'Follow the installation instructions')
                    gevent.thread.interrupt_main()
                    return

                returncode = proc.returncode
                msg = 'attempts' if attempt != 1 else 'attempt'

                if attempt >= 4:
                    logger.critical('aborting after %s %s: rc = %s',
                                    attempt, msg, returncode)
                    gevent.thread.interrupt_main()
                    return

                logger.error('retrying after %s %s: rc = %s',
                             attempt, msg, returncode)
                gevent.sleep(config.SCILAB_INSTANCE_RETRY_INTERVAL * attempt)
                attempt += 1
                FIRST_INSTANCE = True
                continue

            INSTANCES_1.append(instance)
            attempt = 1
            FIRST_INSTANCE = False

        print_scilab_instances()

        if too_many_scilab_instances():
            evt.clear()


def get_scilab_instance():
    global FIRST_INSTANCE

    try:
        while True:
            instance = INSTANCES_1.pop(0)
            proc = instance.proc
            if proc.poll() is not None:
                logger.warning('scilab instance exited: return code is %s',
                               proc.returncode)
                FIRST_INSTANCE = True
                if not too_many_scilab_instances():
                    evt.set()
                    if no_free_scilab_instance():
                        gevent.sleep(4)
                continue

            INSTANCES_2.append(instance)
            print_scilab_instances()
            if not too_many_scilab_instances():
                evt.set()

            return instance
    except IndexError:
        logger.error('No free instance')
        return None


def remove_scilab_instance(instance):
    try:
        INSTANCES_2.remove(instance)
        print_scilab_instances()
        if not too_many_scilab_instances():
            evt.set()
    except ValueError:
        logger.error('could not find instance %s', instance)


def stop_scilab_instance(base, createlogfile=False):
    stop_instance(base.instance, createlogfile)

    base.instance = None


def kill_scilab_with(proc, sig):
    """Send a signal to a Scilab process."""
    try:
        if proc and proc.pid:
            os.kill(proc.pid, sig)
            return True
    except ProcessLookupError:
        print(f"Process {proc.pid} not found.")
    except Exception as e:
        print(f"Error killing Scilab process: {e}")
    return False


def stop_instance(instance, createlogfile=False, removeinstance=True):
    if instance is None:
        logger.warning('no instance')
        return

    if not kill_scilab_with(instance.proc, signal.SIGTERM):
        kill_scilab_with(instance.proc, signal.SIGKILL)

    if removeinstance:
        remove_scilab_instance(instance)

    if instance.log_name is None:
        if createlogfile:
            logger.warning('empty diagram')
    else:
        # remove(instance.log_name)
        instance.log_name = None

    instance.base = None


def stop_scilab_instances():
    if len(INSTANCES_1) > 0:
        logger.info('stopping %s idle instances', len(INSTANCES_1))
        while len(INSTANCES_1) > 0:
            instance = INSTANCES_1.pop()
            stop_instance(instance, removeinstance=False)

    if len(INSTANCES_2) > 0:
        logger.info('stopping %s busy instances', len(INSTANCES_2))
        while len(INSTANCES_2) > 0:
            instance = INSTANCES_2.pop()
            stop_instance(instance, removeinstance=False)


def reap_scilab_instances():
    current_thread().name = 'Reaper'
    while True:
        gevent.sleep(100)

        remove_instances = []

        for instance in INSTANCES_2:
            if instance.endtime < time():
                remove_instances.append(instance)

        count = len(remove_instances)
        if count == 0:
            continue

        logger.info('removing %s stale instances', count)
        for instance in remove_instances:
            base = instance.base
            if base is None:
                logger.warning('cannot stop instance %s', instance)
                stop_instance(instance)
            elif isinstance(base, Diagram):
                kill_scilab(base)
            else:
                logger.warning('cannot stop instance %s', instance)
                stop_instance(instance)


def clean_sessions(final=False):
    current_thread().name = 'Clean'
    totalcount = 0
    cleanuids = []
    for uid, ud in USER_DATA.items():
        totalcount += 1
        if final or time() - ud.timestamp > config.SESSIONTIMEOUT:
            cleanuids.append(uid)

    logger.info('cleaning %s/%s sessions', len(cleanuids), totalcount)
    for uid in cleanuids:
        current_thread().name = 'Clean-%s' % uid[:6]
        try:
            logger.info('cleaning')
            ud = USER_DATA.pop(uid)
            ud.clean()
        except Exception as e:
            logger.warning('could not clean: %s', str(e))


def clean_sessions_thread():
    current_thread().name = 'Clean'
    while True:
        gevent.sleep(config.SESSIONTIMEOUT / 2)
        try:
            clean_sessions()
        except Exception as e:
            logger.warning('Exception in clean_sessions: %s', str(e))


logfilefdrlock = RLock()
LOGFILEFD = 123


def prestart_scilab():
    cmd = SCILAB_START
    cmdarray = [SCILAB,
                "-nogui",
                "-noatomsautoload",
                "-nouserstartup",
                "-nb",
                "-nw",
                "-e", cmd]

    logfilefd, log_name = mkstemp(prefix=datetime.now().strftime(
        'scilab-log-%Y%m%d-'), suffix='.txt', dir=SESSIONDIR)

    with logfilefdrlock:
        if logfilefd != LOGFILEFD:
            os.dup2(logfilefd, LOGFILEFD)
            os.close(logfilefd)

        try:
            proc = subprocess.Popen(
                cmdarray,
                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, start_new_session=True,
                universal_newlines=True, pass_fds=(LOGFILEFD, ))
        except FileNotFoundError:
            logger.critical('scilab has not been built. '
                            'Follow the installation instructions')
            proc = None
            remove(log_name)
            log_name = None

        os.close(LOGFILEFD)

    return (proc, log_name)


def run_scilab(command, base, createlogfile=False, timeout=70):
    instance = get_scilab_instance()
    if instance is None:
        logger.error('cannot run command %s', command)
        return None

    cmd = command + SCILAB_END
    logger.info('running command %s', cmd)
    instance.proc.stdin.write(cmd)

    if not createlogfile:
        remove(instance.log_name)
        instance.log_name = None

    instance.base = base
    instance.starttime = time()
    instance.endtime = time() + timeout
    return instance


def stopDetailsThread(diagram):
    diagram.tkbool = False  # stops the thread
    gevent.sleep(LOOK_DELAY)
    fname = join(diagram.sessiondir, VALUES_FOLDER,
                 diagram.diagram_id + "_*")
    for fn in glob.glob(fname):
        # deletes all files created under the 'diagram_id' name
        remove(fn)


def get_diagram(xcos_file_id, remove=False):
    if not xcos_file_id:
        logger.warning('no id')
        return None
    xcos_file_id = int(xcos_file_id)

    (diagrams, __, __, __, __, __, __) = init_session()

    if xcos_file_id < 0 or xcos_file_id >= len(diagrams):
        logger.warning('id %s not in diagrams', xcos_file_id)
        return None

    diagram = diagrams[xcos_file_id]

    if remove:
        diagrams[xcos_file_id] = Diagram()

    return diagram


def kill_scilab(task_id, diagram=None):
    '''Define function to kill scilab(if still running) and remove files'''
    if diagram is None:
        diagram = get_diagram(task_id, True)

    if diagram is None:
        logger.warning('no diagram')
        return
    logger.info('kill_scilab: diagram=%s', diagram)

    stop_scilab_instance(diagram, True)

    if diagram.xcos_file_name is None:
        logger.warning('empty diagram')
    else:
        # Remove xcos file
        remove(diagram.xcos_file_name)
        diagram.xcos_file_name = None

    if diagram.file_image != '':
        logger.warning('not removing %s', diagram.file_image)

    stopDetailsThread(diagram)


worker = None
reaper = None
cleaner = None


def start_threads():
    global worker, reaper, cleaner
    worker = gevent.spawn(prestart_scilab_instances)
    worker.name = 'PreStart'
    reaper = gevent.spawn(reap_scilab_instances)
    reaper.name = 'Reaper'
    cleaner = gevent.spawn(clean_sessions_thread)
    cleaner.name = 'Clean'


def stop_threads():
    global worker, reaper, cleaner
    gevent.kill(worker)
    worker = None
    gevent.kill(reaper)
    reaper = None
    gevent.kill(cleaner)
    cleaner = None
    clean_sessions(True)
    stop_scilab_instances()
    logger.info('exiting')
