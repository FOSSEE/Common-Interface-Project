from celery import shared_task, states
from celery.exceptions import Ignore
from celery.utils.log import get_task_logger
from redis import Redis
from threading import current_thread
import traceback

from blocks.celery_tasks import app
from simulationAPI.helpers.ngspice_helper import ExecXml, update_task_status
from simulationAPI.models import Task
from simulationAPI.helpers.scilab_manager import uploadscript, getscriptoutput 

logger = get_task_logger(__name__)


def acquire_lock(session_id, timeout=1800):
    redis_client = Redis.from_url(app.conf.broker_url)
    lock = redis_client.lock(f"simulation_lock:{session_id}", timeout=timeout)
    lock.acquire(blocking=True)
    return lock


def release_lock(lock):
    lock.release()


@shared_task(bind=True)
def process_task(self, task_id):
    task = Task.objects.get(task_id=task_id)
    session_id = task.session.session_id
    task_type = task.type
    current_thread().name = f"{session_id[:6]}:{task_id[:8]}"
    lock = acquire_lock(session_id)  # Prevent multiple runs per session

    try:
        logger.info("Processing %s %s %s %s",
                    task_id, task.file.path, task.session.app_name, task.workspace_file)

        update_task_status(task_id, 'STARTED',
                           meta={'current_process': 'Started Processing File'})

        if task_type == 'SCRIPT':
            output = uploadscript(task.session, task)
            state = 'STREAMING'
            current_process = 'Processed Script, Streaming Output'
        else:
            output = ExecXml(task, self.name, task.workspace_file)
            if output == "Streaming":
                state = 'STREAMING'
                current_process = 'Processed Xml, Streaming Output'
            elif output == "Success":
                state = 'SUCCESS'
                current_process = 'Processed Xml, Loading Output'

        update_task_status(task_id, state,
                        meta={'current_process': current_process})
        return output

    except Exception as e:
        update_task_status(task_id, 'FAILURE',
                           meta={
                               'exc_type': type(e).__name__,
                               'exc_message': traceback.format_exc().split('\n')
                           })
        logger.exception('Exception Occurred:')
        raise Ignore()

    finally:
        release_lock(lock)  # Ensure lock is always released


@shared_task
def process_task_script(task_id):
    task = Task.objects.get(task_id=task_id)
    session = task.session
    result = getscriptoutput(session, task)
    update_task_status(task_id, 'SUCCESS', meta=result)
    return result
