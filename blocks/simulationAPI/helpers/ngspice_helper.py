import os
import re
import subprocess
from celery import current_task
from celery.utils.log import get_task_logger
from datetime import datetime
from pathlib import Path
from tempfile import mkstemp
from django.conf import settings

logger = get_task_logger(__name__)
MxGraphParser = os.path.join(settings.BASE_DIR, '../Xcos/MxGraphParser.py')
SCILAB_DIR = os.path.abspath(settings.SCILAB_DIR)
SCILAB = os.path.join(SCILAB_DIR, 'bin', 'scilab-adv-cli')
# handle scilab startup
SCILAB_START = (
    "try;funcprot(0);lines(0,120);"
    "clearfun('messagebox');"
    "function messagebox(msg,title,icon,buttons,modal),disp(msg),endfunction;"
    "funcprot(1);"
    "catch;[error_message,error_number,error_line,error_func]=lasterror();disp(error_message,error_number,error_line,error_func);exit(3);end;"
)

SCILAB_END = "catch;[error_message,error_number,error_line,error_func]=lasterror();disp(error_message,error_number,error_line,error_func);exit(2);end;exit;"
SCILAB_CMD = [SCILAB,
              "-noatomsautoload",
              "-nogui",
              "-nouserstartup",
              "-nb",
              "-nw",
              "-e", SCILAB_START]
LOGFILEFD = 123


class CannotRunParser(Exception):
    """ Base class for exceptions in this module. """


def ExecXml(filepath, file_id, parameters):
    try:
        current_dir = settings.MEDIA_ROOT+'/'+str(file_id)
        # Make Unique Directory for simulation to run
        Path(current_dir).mkdir(parents=True, exist_ok=True)
        os.chdir(current_dir)
        (xcosfilebase, __) = os.path.splitext(filepath)
        xcosfile = xcosfilebase + '.xcos'
        logger.info('will run %s %s', 'MxGraphParser', filepath)
        proc = subprocess.Popen([MxGraphParser, filepath],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                cwd=current_dir)
        (stdout, stderr) = proc.communicate()

        if proc.returncode != 0:
            logger.error('%s error encountered', 'MxGraphParser')
            logger.error(stderr)
            logger.error(proc.returncode)
            logger.error(stdout)
            raise CannotRunParser('exited with error')

        logger.info('Ran %s', 'MxGraphParser')

        (logfilefd, log_name) = mkstemp(prefix=datetime.now().strftime(
                'scilab-log-%Y%m%d-'), suffix='.txt', dir=current_dir)

        if logfilefd != LOGFILEFD:
            os.dup2(logfilefd, LOGFILEFD)
            os.close(logfilefd)

        logger.info('will run %s %s> %s', SCILAB_CMD[0], LOGFILEFD, log_name)
        logger.info('running command %s', SCILAB_CMD[-1])
        proc = subprocess.Popen(
            SCILAB_CMD,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            start_new_session=True, universal_newlines=True, cwd=current_dir,
            pass_fds=(LOGFILEFD, ))

        os.close(LOGFILEFD)

        current_task.update_state(
            state='STREAMING',
            meta={'current_process': 'Processed Xml, Streaming Output'})

        cmd = "try;"
        cmd += "chdir('%s');" % current_dir
        cmd += "loadXcosLibs();"
        xcosfile = '/tmp/blocks-tmp/Ex3_1.xcos' # FIXME: remove this line
        cmd += "importXcosDiagram('%s');" % xcosfile
        cmd += "xcos_simulate(scs_m,4);"
        cmd += SCILAB_END

        logger.info('running command %s', cmd)
        proc.stdin.write(cmd)

        (out, err) = proc.communicate()

        maxlines = 15
        logger.info('Ran %s', SCILAB_CMD[0])
        if out:
            out = out.rstrip()
            if out:
                out = '\n'.join(re.split(r'\n+', out, maxlines + 1)[:maxlines])
                logger.info('out=%s', out)
        if err:
            err = err.rstrip()
            if err:
                err = '\n'.join(re.split(r'\n+', err, maxlines + 1)[:maxlines])
                logger.info('err=%s', err)

        log_name = '/tmp/blocks-tmp/scilab-log.txt' # FIXME: remove this line
        return ('Streaming', log_name, proc.returncode)
    except BaseException as e:
        logger.exception('Encountered Exception:')
        logger.info('removing %s', filepath)
        os.remove(filepath)
        target = os.listdir(current_dir)
        for item in target:
            logger.info('removing %s', item)
            os.remove(os.path.join(current_dir, item))
        logger.info('removing %s', current_dir)
        os.rmdir(current_dir)
        logger.info('Deleted Files')
        raise e
