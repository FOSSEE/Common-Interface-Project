from celery.utils.log import get_task_logger
from datetime import datetime
from django.conf import settings
from django.http import FileResponse, Http404, JsonResponse
import gevent
from gevent.event import Event
from gevent.lock import RLock
import glob
import json
import logging
import os
from os.path import abspath, exists, isfile, join
import re
import signal
import subprocess
from tempfile import mkdtemp, mkstemp
from threading import current_thread
from time import time
import unicodedata
import uuid

from simulationAPI.helpers import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blocks.settings')

# Scilab dir
SCILAB_DIR = abspath(settings.SCILAB_DIR)
SCILAB = join(SCILAB_DIR, 'bin', 'scilab-adv-cli')
BASEDIR = abspath('src/static')
IMAGEDIR = join(BASEDIR, config.IMAGEDIR)


SESSIONDIR = abspath(config.SESSIONDIR)
SYSTEM_COMMANDS = re.compile(config.SYSTEM_COMMANDS)
SPECIAL_CHARACTERS = re.compile(config.SPECIAL_CHARACTERS)

# This is the path to the upload directory and values directory
UPLOAD_FOLDER = 'uploads'  # to store xcos file
VALUES_FOLDER = 'values'  # to store files related to tkscale block
# to store uploaded sci files for sci-func block
SCRIPT_FILES_FOLDER = 'script_files'
# to store workspace files for TOWS_c block
WORKSPACE_FILES_FOLDER = 'workspace_files'

# Delay time to look for new line (in s)
LOOK_DELAY = 0.1

# display limit for long strings
DISPLAY_LIMIT = 10
# handle scilab startup
SCILAB_START = (
    "try;funcprot(0);lines(0,120);"
    "clearfun('messagebox');"
    "function messagebox(msg,title,icon,buttons,modal),disp(msg),endfunction;"
    "function xinfo(msg),disp(msg),endfunction;"
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


def secure_filename(filename: str) -> str:
    filename = unicodedata.normalize("NFKD", filename)
    filename = filename.encode("ascii", "ignore").decode("ascii")  # Remove accents
    filename = re.sub(r"[^a-zA-Z0-9_.-]", "_", filename)  # Replace invalid characters
    return filename.strip("._")  # Prevent filenames like ".." or "."


def makedirs(dirname, dirtype):
    if not exists(dirname):
        os.makedirs(dirname)


def rmdir(dirname, dirtype):
    try:
        if exists(dirname):
            os.rmdir(dirname)
    except Exception as e:
        logger.warning('could not remove %s: %s', dirname, str(e))


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


worker_logger = logging.getLogger("celery")
logger = get_task_logger(__name__)

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


class Script:
    script_id = None
    sessiondir = None
    filename = None
    status = 0
    instance = None
    workspace_filename = None

    def __str__(self):
        return (
            "{script_id: %s, filename: %s, status: %d, instance: %s, "
            "workspace_filename: %s}") % (
                self.script_id, self.filename, self.status, self.instance,
                self.workspace_filename)

    def clean(self):
        if self.instance is not None:
            kill_script(self)
            self.instance = None
        if self.filename is not None:
            remove(self.filename)
            self.filename = None
        if self.workspace_filename is not None:
            remove(self.workspace_filename)
            self.workspace_filename = None


class SciFile:
    '''Variables used in sci-func block'''
    instance = None

    def clean(self):
        if self.instance is not None:
            kill_scifile(self)
            self.instance = None


class UserData:
    sessiondir = None
    diagrams = None
    scripts = None
    datafiles = None
    scriptcount = None
    scifile = None
    diagramlock = None
    timestamp = None

    def __init__(self):
        self.sessiondir = mkdtemp(
            prefix=datetime.now().strftime('%Y%m%d.'), dir=SESSIONDIR)
        self.diagrams = []
        self.datafiles = []
        self.scripts = {}
        self.scriptcount = 0
        self.scifile = SciFile()
        self.diagramlock = RLock()
        self.timestamp = time()

    def getscriptcount(self):
        with self.diagramlock:
            rv = self.scriptcount
            self.scriptcount += 1

        return str(rv)

    def clean(self):
        for diagram in self.diagrams:
            diagram.clean()
        self.diagrams = None
        for script in self.scripts:
            self.scripts[script].clean()
        self.scripts = None
        for datafile in self.datafiles:
            datafile.clean()
        self.datafiles = None
        self.scifile.clean()
        self.scifile = None
        self.diagramlock = None
        # name of workspace file
        workspace = join(self.sessiondir, WORKSPACE_FILES_FOLDER,
                         "workspace.dat")
        if exists(workspace):
            remove(workspace)

        sessiondir = self.sessiondir

        rmdir(join(sessiondir, WORKSPACE_FILES_FOLDER), 'workspace files')
        rmdir(join(sessiondir, SCRIPT_FILES_FOLDER), 'script files')
        rmdir(join(sessiondir, VALUES_FOLDER), 'values')
        rmdir(join(sessiondir, UPLOAD_FOLDER), 'upload')
        rmdir(sessiondir, 'session')


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
        worker_logger.info('can start %s instances', lssi)
    return lssi


def print_scilab_instances():
    l1 = len(INSTANCES_1)
    l2 = len(INSTANCES_2)
    msg = ''
    if l1 > 0:
        msg += ', free=' + str(l1)
    if l2 > 0:
        msg += ', in use=' + str(l2)
    worker_logger.info('instance count: %s', msg[2:])


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
    '''
    function to kill a process group with a signal. wait for maximum 2 seconds
    for process to exit. return True on exit, False otherwise
    '''

    if proc.poll() is not None:
        return True

    try:
        os.killpg(proc.pid, sig)
    except OSError:
        logger.warning('could not kill %s with signal %s', proc.pid, sig)
        return False
    except TypeError:
        logger.warning('could not kill invalid process %s with signal %s', proc.pid, sig)
        return True
    except ProcessLookupError:
        logger.warning('could not find process %s to kill with signal %s', proc.pid, sig)
        return True
    except Exception as e:
        logger.warning('Error killing process %s with signal %s', proc.pid, sig, e)

    for i in range(0, 20):
        gevent.sleep(LOOK_DELAY)
        if proc.poll() is not None:
            return True
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
        worker_logger.info('stopping %s idle instances', len(INSTANCES_1))
        while len(INSTANCES_1) > 0:
            instance = INSTANCES_1.pop()
            stop_instance(instance, removeinstance=False)

    if len(INSTANCES_2) > 0:
        worker_logger.info('stopping %s busy instances', len(INSTANCES_2))
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

        worker_logger.info('removing %s stale instances', count)
        for instance in remove_instances:
            base = instance.base
            if base is None:
                worker_logger.warning('cannot stop instance %s', instance)
                stop_instance(instance)
            elif isinstance(base, Diagram):
                kill_scilab(base)
            elif isinstance(base, Script):
                kill_script(base)
            elif isinstance(base, SciFile):
                kill_scifile(base)
            else:
                worker_logger.warning('cannot stop instance %s', instance)
                stop_instance(instance)


class DataFile:
    sessiondir = None
    data_filename = None

    def clean(self):
        if self.data_filename is not None:
            remove(self.data_filename)
            self.data_filename = None


def clean_sessions(final=False):
    current_thread().name = 'Clean'
    totalcount = 0
    cleanuids = []
    for uid, ud in USER_DATA.items():
        totalcount += 1
        if final or time() - ud.timestamp > config.SESSIONTIMEOUT:
            cleanuids.append(uid)

    worker_logger.info('cleaning %s/%s sessions', len(cleanuids), totalcount)
    for uid in cleanuids:
        current_thread().name = 'Clean-%s' % uid[:6]
        try:
            worker_logger.info('cleaning')
            ud = USER_DATA.pop(uid)
            ud.clean()
        except Exception as e:
            worker_logger.warning('could not clean: %s', str(e))


def clean_sessions_thread():
    current_thread().name = 'Clean'
    while True:
        gevent.sleep(config.SESSIONTIMEOUT / 2)
        try:
            clean_sessions()
        except Exception as e:
            worker_logger.warning('Exception in clean_sessions: %s', str(e))


logfilefdrlock = RLock()
LOGFILEFD = 123


def set_session(session):
    if 'uid' not in session:
        session['uid'] = str(uuid.uuid4())

    uid = session['uid']
    if not hasattr(current_thread(), 's_name'):
        current_thread().s_name = current_thread().name
    current_thread().name = 'S-%s-%s' % (current_thread().s_name[12:], uid[:6])
    return uid


def init_session():
    uid = set_session()

    if uid not in USER_DATA:
        USER_DATA[uid] = UserData()

    ud = USER_DATA[uid]
    ud.timestamp = time()

    sessiondir = ud.sessiondir

    makedirs(sessiondir, 'session')
    makedirs(join(sessiondir, UPLOAD_FOLDER), 'upload')
    makedirs(join(sessiondir, VALUES_FOLDER), 'values')
    makedirs(join(sessiondir, SCRIPT_FILES_FOLDER), 'script files')
    makedirs(join(sessiondir, WORKSPACE_FILES_FOLDER), 'workspace files')

    return (ud.diagrams, ud.scripts, ud.getscriptcount, ud.scifile,
            ud.datafiles, sessiondir, ud.diagramlock)


def prestart_scilab():
    logfilefd, log_name = mkstemp(prefix=datetime.now().strftime(
        'scilab-log-%Y%m%d-'), suffix='.txt', dir=SESSIONDIR)

    with logfilefdrlock:
        if logfilefd != LOGFILEFD:
            os.dup2(logfilefd, LOGFILEFD)
            os.close(logfilefd)

        try:
            proc = subprocess.Popen(
                SCILAB_CMD,
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


def is_unsafe_script(filename):
    '''
    Read file and check for system commands and return error if file contains
    system commands
    '''
    with open(filename, 'r') as f:
        if not re.search(SYSTEM_COMMANDS, f.read()):
            return False

    # Delete saved file if system commands are encountered in that file
    remove(filename)
    return True


def uploaddatafile(request):
    '''
    Below route is called for uploading audio/other file.
    '''
    # Get the au/other data file
    file = request.files['file']
    # Check if the data file is not null
    if not file:
        msg = "Error occured while uploading file. Please try again\n"
        rv = {'msg': msg}
        return JsonResponse(rv)

    (datafile, sessiondir, currlen) = add_datafile()
    fname = join(sessiondir, UPLOAD_FOLDER, currlen + '@@' + secure_filename(file.filename))
    file.save(fname)
    datafile.data_filename = fname
    rv = {'filepath': datafile.data_filename}
    return JsonResponse(rv)


def uploadscript(request):
    '''
    Below route is called for uploading script file.
    '''
    (script, sessiondir) = add_script()

    file = request.files['file']
    if not file:
        msg = "Upload Error\n"
        rv = {'msg': msg}
        return JsonResponse(rv)

    fname = join(sessiondir, SCRIPT_FILES_FOLDER,
                 script.script_id + '_script.sce')
    file.save(fname)
    script.filename = fname

    if is_unsafe_script(fname):
        msg = ("System calls are not allowed in script.\n"
               "Please edit the script again.\n")
        script.status = -1
        rv = {'status': script.status, 'msg': msg}
        return JsonResponse(rv)

    wfname = join(sessiondir, SCRIPT_FILES_FOLDER,
                  script.script_id + '_script_workspace.dat')
    script.workspace_filename = wfname
    command = "exec('%s');save('%s');" % (fname, wfname)

    script.instance = run_scilab(command, script)

    if script.instance is None:
        msg = "Resource not available"
        script.status = -2
        rv = {'status': script.status, 'msg': msg}
        return JsonResponse(rv)

    msg = ''
    script.status = 1
    rv = {'script_id': script.script_id, 'status': script.status, 'msg': msg}
    return JsonResponse(rv)


def clean_output(s):
    '''handle whitespace and sequences in output'''
    s = re.sub(r'[\a\b\f\r\v]', r'', s)
    # https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_sequences
    s = re.sub(r'\x1b\[[\x30-\x3f]*[\x20-\x2f]*[\x40-\x7e]', r'', s)
    s = re.sub(r'\t', r'    ', s)
    s = re.sub(r' +(\n|$)', r'\n', s)
    s = re.sub(r'\n+', r'\n', s)
    s = re.sub(r'^\n', r'', s)
    return s


def load_variables(filename):
    '''
    add scilab commands to load only user defined variables
    '''

    command = "[__V1,__V2]=listvarinfile('%s');" % filename
    command += "__V5=grep(string(__V2),'/^([124568]|1[07])$/','r');"
    command += "__V1=__V1(__V5);"
    command += "__V2=__V2(__V5);"
    command += "__V5=grep(__V1,'/^[^%]+$/','r');"
    command += "if ~isempty(__V5) then;"
    command += "__V1=__V1(__V5);"
    command += "__V2=__V2(__V5);"
    command += "__V6=''''+strcat(__V1,''',''')+'''';"
    command += "__V7='load(''%s'','+__V6+');';" % filename
    command += "execstr(__V7);"
    command += "end;"
    command += "clear __V1 __V2 __V5 __V6 __V7;"
    return command


def start_scilab():
    '''
    function to execute xcos file using scilab (scilab-adv-cli), access log
    file written by scilab
    '''
    diagram = get_diagram(get_request_id())
    if diagram is None:
        logger.warning('no diagram')
        return "error"

    # name of primary workspace file
    workspace_filename = diagram.workspace_filename
    # name of workspace file
    workspace = join(diagram.sessiondir, WORKSPACE_FILES_FOLDER,
                     "workspace.dat")

    if diagram.workspace_counter in (2, 3) and not exists(workspace):
        logger.warning('no workspace')
        return ("Workspace does not exist. "
                "Please simulate a diagram with TOWS_c block first. "
                "Do not use any FROMWSB block in that diagram.")

    loadfile = workspace_filename is not None or \
        diagram.workspace_counter in (2, 3)

    command = ""

    if loadfile:
        # ignore import errors
        command += "try;"

        if workspace_filename is not None:
            command += load_variables(workspace_filename)

        if diagram.workspace_counter in (2, 3):
            # 3 - for both TOWS_c and FROMWSB and also workspace dat file exist
            # In this case workspace is saved in format of dat file (Scilab way
            # of saying workpsace)
            # For FROMWSB block and also workspace dat file exist
            command += load_variables(workspace)

        command += "catch;disp('Error: ' + lasterror());end;"

    # Scilab Commands for running of scilab based on existence of different
    # blocks in same diagram from workspace_counter's value
    #    1: Indicate TOWS_c exist
    #    2: Indicate FROMWSB exist
    #    3: Both TOWS_c and FROMWSB exist
    #    4: Indicate AFFICH_m exist (We dont want graphic window to open so
    #    xs2jpg() command is removed)
    #    5: Indicate Sci-func block as it some time return image as output
    #    rather than Sinks's log file.
    #    0/No-condition : For all other blocks

    command += "loadXcosLibs();"
    command += "importXcosDiagram('%s');" % diagram.xcos_file_name
    command += "xcos_simulate(scs_m,4);"

    if diagram.workspace_counter == 4:
        # For AFFICH-m block
        pass
    elif diagram.workspace_counter == 5:
        # For Sci-Func block (Image are return as output in some cases)
        diagram.file_image = 'img-%s-%s.jpg' % (
            datetime.now().strftime('%Y%m%d'), str(uuid.uuid4()))
        command += "xs2jpg(gcf(),'%s/%s');" % (IMAGEDIR, diagram.file_image)
    elif config.CREATEIMAGE:
        # For all other block
        command += "xs2jpg(gcf(),'%s/%s');" % (IMAGEDIR, 'img_test.jpg')

    if diagram.workspace_counter in (1, 3):
        if diagram.save_variables:
            command += "save('%s','%s');" % (
                workspace, "','".join(diagram.save_variables))
        else:
            command += "save('%s');" % workspace

    diagram.instance = run_scilab(command, diagram, True,
                                  config.SCILAB_INSTANCE_TIMEOUT_INTERVAL + 60)

    if diagram.instance is None:
        return "Resource not available"

    instance = diagram.instance
    logger.info('log_name=%s', instance.log_name)

    # Start sending log to chart function for creating chart
    try:
        # For processes taking less than 10 seconds
        scilab_out = instance.proc.communicate(timeout=4)[0]
        scilab_out = re.sub(r'^[ !\\-]*\n', r'',
                            scilab_out, flags=re.MULTILINE)
        if scilab_out:
            logger.info('=== Output from scilab console ===\n%s', scilab_out)
        # Check for errors in Scilab
        if "Empty diagram" in scilab_out:
            remove_scilab_instance(diagram.instance)
            diagram.instance = None
            return "Empty diagram"

        m = re.search(r'Fatal error: exception Failure\("([^"]*)"\)',
                      scilab_out)
        if m:
            msg = 'modelica error: ' + m.group(1)
            remove_scilab_instance(diagram.instance)
            diagram.instance = None
            return msg

        if ("xcos_simulate: "
                "Error during block parameters update.") in scilab_out:
            remove_scilab_instance(diagram.instance)
            diagram.instance = None
            return "Error in block parameter. Please check block parameters"

        if "xcosDiagramToScilab:" in scilab_out:
            remove_scilab_instance(diagram.instance)
            diagram.instance = None
            return "Error in xcos diagram. Please check diagram"

        if "Simulation problem:" in scilab_out:
            remove_scilab_instance(diagram.instance)
            diagram.instance = None
            return "Error in simulation. Please check script uploaded/executed"

        if "Cannot find scilab-bin" in scilab_out:
            remove_scilab_instance(diagram.instance)
            diagram.instance = None
            return ("scilab has not been built. "
                    "Follow the installation instructions")

        if os.stat(instance.log_name).st_size == 0 and \
                diagram.workspace_counter not in (1, 5):
            remove_scilab_instance(diagram.instance)
            diagram.instance = None
            return "log file is empty"

    # For processes taking more than 10 seconds
    except subprocess.TimeoutExpired:
        pass

    return ""


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


def add_diagram():
    (diagrams, scripts, __, __, __, sessiondir, diagramlock) = init_session()

    with diagramlock:
        diagram = Diagram()
        diagram.diagram_id = str(len(diagrams))
        diagram.sessiondir = sessiondir
        diagrams.append(diagram)

    return (diagram, scripts, sessiondir)


def get_script(script_id, scripts=None, remove=False):
    if script_id is None:
        return None
    if not script_id:
        logger.warning('no id')
        return None

    if scripts is None:
        (__, scripts, __, __, __, __, __) = init_session()

    if script_id not in scripts:
        logger.warning('id %s not in scripts', script_id)
        return None

    script = scripts[script_id]

    if remove:
        del scripts[script_id]

    return script


def add_script():
    (__, scripts, getscriptcount, __, __, sessiondir, __) = init_session()

    script_id = getscriptcount()

    script = Script()
    script.script_id = script_id
    script.sessiondir = sessiondir
    scripts[script_id] = script

    return (script, sessiondir)


def add_datafile():
    (__, __, __, __, datafiles, sessiondir, __) = init_session()

    datafile = DataFile()
    datafile.sessiondir = sessiondir
    datafiles.append(datafile)

    return (datafile, sessiondir, str(len(datafiles)))


def DownloadFile(request):
    '''route for download of binary and audio'''
    fn = request.form['path']
    if fn == '' or fn[0] == '.' or '/' in fn:
        logger.warning('downloadfile=%s', fn)
        return "error"
    # check if audio file or binary file
    if "audio" in fn:
        mimetype = 'audio/basic'
    else:
        mimetype = 'application/octet-stream'
    file_path = os.path.join(SESSIONDIR, fn)
    if not os.path.exists(file_path):
        raise Http404("File not found")
    return FileResponse(open(file_path, 'r'),
                        as_attachment=True, mimetype=mimetype)


def DeleteFile(request):
    '''route for deletion of binary and audio file'''
    fn = request.form['path']
    if fn == '' or fn[0] == '.' or '/' in fn:
        logger.warning('deletefile=%s', fn)
        return "error"
    remove(fn)  # deleting the file
    return "0"


def get_request_id(request, key='id'):
    args = request.args
    if args is None:
        logger.warning('No args in request')
        return ''
    if key not in args:
        logger.warning('No %s in request.args', key)
        return ''
    value = args[key]
    if re.fullmatch(r'[0-9]+', value):
        return value
    displayvalue = value if len(
        value) <= DISPLAY_LIMIT + 3 else value[:DISPLAY_LIMIT] + '...'
    logger.warning('Invalid value %s for %s in request.args',
                   displayvalue, key)
    return ''


def get_script_id(request, key='script_id', default=''):
    form = request.form
    if form is None:
        logger.warning('No form in request')
        return default
    if key not in form:
        logger.warning('No %s in request.form', key)
        return default
    value = form[key]
    if re.fullmatch(r'[0-9]+', value):
        return value
    displayvalue = value if len(
        value) <= DISPLAY_LIMIT + 3 else value[:DISPLAY_LIMIT] + '...'
    logger.warning('Invalid value %s for %s in request.form',
                   displayvalue, key)
    return default


def internal_fun(request, internal_key):
    (__, __, __, scifile, __, sessiondir, __) = init_session()

    if internal_key not in config.INTERNAL:
        msg = internal_key + ' not found'
        logger.warning(msg)
        return JsonResponse({'msg': msg})
    internal_data = config.INTERNAL[internal_key]

    cmd = ""
    for scriptfile in internal_data['scriptfiles']:
        cmd += "exec('%s');" % scriptfile
    file_name = join(sessiondir, internal_key + ".txt")
    function = internal_data['function']
    parameters = internal_data['parameters']
    if 'num' in parameters:
        p = 's'
        cmd += "%s=poly(0,'%s');" % (p, p)
        p = 'z'
        cmd += "%s=poly(0,'%s');" % (p, p)
    cmd += "%s('%s'" % (function, file_name)
    for parameter in parameters:
        if parameter not in request.form:
            msg = parameter + ' parameter is missing'
            logger.warning(msg)
            return JsonResponse({'msg': msg})
        value = request.form[parameter]
        try:
            value.encode('ascii')
        except UnicodeEncodeError:
            msg = parameter + ' parameter has non-ascii value'
            logger.warning(msg)
            return JsonResponse({'msg': msg})
        if re.search(SYSTEM_COMMANDS, value):
            msg = parameter + ' parameter has unsafe value'
            logger.warning(msg)
            return JsonResponse({'msg': msg})
        if re.search(SPECIAL_CHARACTERS, value):
            msg = parameter + ' parameter has value with special characters'
            logger.warning(msg)
            return JsonResponse({'msg': msg})
        if 'num' in parameters:
            cmd += ",%s" % value
        else:
            cmd += ",'%s'" % value
    cmd += ");"

    if scifile.instance is not None:
        msg = 'Cannot execute more than one script at the same time.'
        return JsonResponse({'msg': msg})

    scifile.instance = run_scilab(cmd, scifile)
    if scifile.instance is None:
        msg = "Resource not available"
        return JsonResponse({'msg': msg})

    proc = scifile.instance.proc
    (out, err) = proc.communicate()
    out = re.sub(r'^[ !\\-]*\n', r'', out, flags=re.MULTILINE)
    if out:
        logger.info('=== Output from scilab console ===\n%s', out)
    if err:
        logger.info('=== Error from scilab console ===\n%s', err)
    remove_scilab_instance(scifile.instance)
    scifile.instance = None

    if not isfile(file_name):
        msg = "Output file not available"
        logger.warning(msg)
        return JsonResponse({'msg': msg})

    with open(file_name) as f:
        data = f.read()  # Read the data into a variable

    remove(file_name)

    return data


def clean_text(s):
    return re.sub(r'[ \t]*[\r\n]+[ \t]*', r'', s)


def clean_text_2(s, forindex):
    '''handle whitespace'''
    s = re.sub(r'[\a\b\f\r\v]', r'', s)
    s = re.sub(r'\t', r'    ', s)
    s = re.sub(r' +(\n|$)', r'\n', s)
    if forindex:
        s = re.sub(r'\n+$', r'', s)
        # double each backslash
        s = re.sub(r'\\', r'\\\\', s)
        # replace each newline with '\n'
        s = re.sub(r'\n', r'\\n', s)
    else:
        s = re.sub(r'\n{2,}$', r'\n', s)
    return s


def kill_scilab(diagram=None):
    '''Define function to kill scilab(if still running) and remove files'''
    if diagram is None:
        diagram = get_diagram(get_request_id(), True)

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


def kill_script(script=None):
    '''Below route is called for stopping a running script file.'''
    if script is None:
        script = get_script(get_script_id(), remove=True)
        if script is None:
            # when called with same script_id again or with incorrect script_id
            logger.warning('no script')
            return "error"

    logger.info('kill_script: script=%s', script)

    stop_scilab_instance(script)

    if script.filename is None:
        logger.warning('empty script')
    else:
        remove(script.filename)
        script.filename = None

    if script.workspace_filename is None:
        logger.warning('empty workspace')
    else:
        remove(script.workspace_filename)
        script.workspace_filename = None

    return "ok"


def kill_scifile(scifile=None):
    '''Below route is called for stopping a running sci file.'''
    if scifile is None:
        (__, __, __, scifile, __, __, __) = init_session()

    logger.info('kill_scifile: scifile=%s', scifile)

    stop_scilab_instance(scifile)

    return "ok"


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
    worker_logger.info('exiting')
