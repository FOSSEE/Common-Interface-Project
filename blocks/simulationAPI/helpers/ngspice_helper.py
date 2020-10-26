import os
import logging
import subprocess
from pathlib import Path
from django.conf import settings
from .parse import extract_data_from_ngspice_output

logger = logging.getLogger(__name__)
MxGraphParser = os.path.join(settings.BASE_DIR, '../Xcos/MxGraphParser.py')
XcosDir = os.path.join(settings.BASE_DIR, '../Xcos/')
SCILAB_DIR = os.path.abspath(settings.SCILAB_DIR)
SCILAB = os.path.join(SCILAB_DIR, 'bin', 'scilab-cli')
# handle scilab startup
SCILAB_START = (
    "try;funcprot(0);lines(0,120);"
    "clearfun('messagebox');"
    "function messagebox(msg,title,icon,buttons,modal),disp(msg),endfunction;"
    "funcprot(1);chdir('%s');exec('Xcos.sci');"
    "catch;[error_message,error_number,error_line,error_func]=lasterror();disp(error_message,error_number,error_line,error_func);exit(3);end;"
) % XcosDir

SCILAB_END = "catch;[error_message,error_number,error_line,error_func]=lasterror();disp(error_message,error_number,error_line,error_func);exit(2);end;exit;"
SCILAB_CMD = [SCILAB,
              "-noatomsautoload",
              "-nouserstartup",
              "-nb",
              "-e", SCILAB_START]


class CannotRunParser(Exception):
    """Base class for exceptions in this module."""
    pass


def ExecXml(filepath, file_id):
    if not os.path.isfile(filepath):
        raise IOError
    try:

        current_dir = settings.MEDIA_ROOT+'/'+str(file_id)
        # Make Unique Directory for simulation to run
        Path(current_dir).mkdir(parents=True, exist_ok=True)
        os.chdir(current_dir)
        (scifilebase, __) = os.path.splitext(filepath)
        scifile = scifilebase + '.sci'
        logger.info('will run %s %s %s > %s', 'MxGraphParser', filepath, current_dir, scifile)
        with open(scifile, 'w') as scifp:
            proc = subprocess.Popen([MxGraphParser, filepath, current_dir],
                                    stdout=scifp, stderr=subprocess.PIPE,
                                    cwd=current_dir)
            stdout, stderr = proc.communicate()

            if proc.returncode not in [0, 1]:
                logger.error('%s error encountered', 'MxGraphParser')
                logger.error(stderr)
                logger.error(proc.returncode)
                logger.error(stdout)
                raise CannotRunParser('exited with error')

            logger.info('Ran %s', 'MxGraphParser')

        logger.info('running command %s', SCILAB_CMD[-1])
        proc = subprocess.Popen(
            SCILAB_CMD,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            start_new_session=True, universal_newlines=True, cwd=current_dir)

        cmd = "try;chdir('%s');exec('%s');%s" % (current_dir, scifile, SCILAB_END)
        logger.info('running command %s', cmd)
        proc.stdin.write(cmd)

        stdout, stderr = proc.communicate()

        logger.info('Ran %s', SCILAB_CMD[0])

        return "Success"
    except Exception as e:
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
