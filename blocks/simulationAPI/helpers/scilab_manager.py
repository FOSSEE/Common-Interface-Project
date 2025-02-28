from gevent.monkey import patch_all

patch_all(aggressive=False, subprocess=True)

import os
import re
import time
import signal
import logging
import subprocess
import gevent
from gevent.event import Event
from gevent.lock import RLock
from threading import current_thread


SCILAB_MIN_INSTANCES = int(os.environ.get('SCILAB_MIN_INSTANCES', '1'))
SCILAB_MAX_INSTANCES = int(os.environ.get('SCILAB_MAX_INSTANCES', '3'))
SCILAB_START_INSTANCES = int(os.environ.get('SCILAB_START_INSTANCES', '2'))
SCILAB_INSTANCE_RETRY_INTERVAL = int(os.environ.get('SCILAB_INSTANCE_RETRY_INTERVAL', '15'))


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


INSTANCES_1 = []
INSTANCES_2 = []
evt = Event()


def prestart_scilab():
    try:
        proc = subprocess.Popen(["scilab-adv-cli", "-noatomsautoload", "-nb"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log_name = "scilab_log.txt"
        return proc, log_name
    except Exception as e:
        print("Error starting Scilab:", e)
        return None, None


def no_free_scilab_instance():
    l1 = len(INSTANCES_1)
    return l1 == 0


def too_many_scilab_instances():
    l1 = len(INSTANCES_1)
    l2 = len(INSTANCES_2)
    return l1 >= SCILAB_MIN_INSTANCES or \
        l1 + l2 >= SCILAB_MAX_INSTANCES


def start_scilab_instances():
    l1 = len(INSTANCES_1)
    l2 = len(INSTANCES_2)
    lssi = min(SCILAB_START_INSTANCES,
               SCILAB_MAX_INSTANCES - l2) - l1
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


def clean_sessions_thread():
    # Ensure this function exists
    print("Cleaning sessions...")


def clean_sessions(force=False):
    print("Cleaning sessions...")


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
                gevent.sleep(SCILAB_INSTANCE_RETRY_INTERVAL * attempt)
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
            else:
                logger.warning('cannot stop instance %s', instance)
                stop_instance(instance)
