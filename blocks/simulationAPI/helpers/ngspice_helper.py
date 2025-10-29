import json
import os
from os.path import join, splitext
import re
import subprocess
from celery import current_task
from celery.utils.log import get_task_logger
from datetime import datetime
from pathlib import Path
from tempfile import mkstemp
from django.conf import settings
from django.db.models import Case, F, Value, When
from django.utils.timezone import now

from simulationAPI.models import Task
from simulationAPI.helpers.scilab_manager import start_scilab, upload, remove, rmdir

logger = get_task_logger(__name__)
XmlToXcos = join(settings.BASE_DIR, 'Xcos/XmlToXcos.sh')

START_STATES = ["STARTED"]
END_STATES = ["SUCCESS", "FAILURE", "CANCELED"]


class CannotRunParser(Exception):
    """ Base class for exceptions in this module. """


def validate_file_path(file_path):
    logger.info(f"Validating file path {file_path}")
    if not re.match(r'^[\w\-./]+$', file_path):
        return False

    if re.match(r'[/.][/.]', file_path):
        return False

    if not file_path.startswith(settings.FILE_STORAGE_ROOT):
        return False

    return True


def update_task_status(task, task_id, status, meta=None):
    # Update Celery backend state
    if task is not None:
        try:
            task.update_state(state=status, meta=meta or {})
        except Exception as e:
            logger.error(f"Error updating Celery task state: {e}")

    # Update Django database
    if task_id is not None:
        Task.objects.filter(task_id=task_id).update(
            status=status,
            start_time=Case(
                When(status__in=START_STATES, then=Value(now())),
                default=F("start_time")
            ),
            end_time=Case(
                When(status__in=END_STATES, then=Value(now())),
                default=F("end_time")
            )
        )


def CreateXml(file_path, parameters, task_id, workspace_file):
    if not validate_file_path(file_path):
        logger.error(f"Invalid file path detected: {file_path}")
        raise CannotRunParser("Invalid file path.")

    parameters = json.loads(parameters)
    current_dir = settings.MEDIA_ROOT + '/' + str(task_id)
    # Make Unique Directory for simulation to run
    Path(current_dir).mkdir(parents=True, exist_ok=True)
    try:
        (xcosfilebase, __) = splitext(file_path)
        xcosfile = xcosfilebase + '.xcos'
        logger.info('will run %s %s %s', 'XmlToXcos', file_path, workspace_file)
        if workspace_file is None:
            workspace_file = ''
        proc = subprocess.Popen([XmlToXcos, file_path, workspace_file],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout, stderr) = proc.communicate()

        if proc.returncode != 0:
            logger.error('%s error encountered', 'XmlToXcos')
            logger.error('rv=%s', proc.returncode)
            msg = 'exited with error'
            if stdout:
                logger.info('Stdout:\n%s', stdout.decode())
            if stderr:
                stderr = stderr.decode()
                logger.error('Stderr:\n%s', stderr)
                # Get last non-empty line from stderr
                last_line = next((line for line in reversed(stderr.strip().splitlines()) if line.strip()), None)
                if last_line:
                    msg = last_line
            raise CannotRunParser(msg)

        logger.info('Ran %s', 'XmlToXcos')
        return xcosfile
    except Exception as e:
        logger.exception('Encountered Exception:')
        logger.info('removing %s', file_path)
        remove(file_path)
        target = os.listdir(current_dir)
        for item in target:
            logger.info('removing %s', item)
            remove(join(current_dir, item))
        logger.info('removing %s', current_dir)
        rmdir(current_dir)
        logger.info('Deleted Files')
        raise e


def CreateXcos(file_path, parameters, task_id, workspace_file):
    xcosfile = CreateXml(file_path, parameters, task_id, workspace_file)
    return xcosfile


def ExecXml(task, task_name, workspace_file):
    task_id = task.task_id
    file_path = task.file.path

    current_dir = settings.MEDIA_ROOT + '/' + str(task_id)
    try:
        # Create xcos file
        xcosfile = CreateXml(file_path, task.parameters, task_id, workspace_file)

        upload(task.session, task, xcosfile)
        result = start_scilab(task.session, task, xcosfile)

        if result == "":
            logger.info('Simulation completed successfully for task %s', task_id)
            return 'Streaming'
        else:
            logger.warning('Simulation failed for task %s: %s', task_id, result)
            return 'Failure'

    except Exception as e:
        logger.exception('Encountered Exception during XML Execution:')
        logger.info('Cleaning up files for task %s', task_id)
        # Cleanup
        remove(file_path)
        target = os.listdir(current_dir)
        for item in target:
            remove(join(current_dir, item))
        rmdir(current_dir)
        logger.info('Deleted Files and Directory for task %s', task_id)
        raise e
