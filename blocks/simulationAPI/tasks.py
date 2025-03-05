from celery import shared_task, current_task, states
from celery.exceptions import Ignore
from celery.utils.log import get_task_logger
from redis import Redis
import traceback

from blocks.celery_tasks import app
from simulationAPI.helpers import ngspice_helper
from simulationAPI.models import Task

logger = get_task_logger(__name__)


def acquire_lock(session_id, timeout=1800):
    redis_client = Redis.from_url(app.conf.broker_url)
    lock = redis_client.lock(f"simulation_lock:{session_id}", timeout=timeout)
    lock.acquire(blocking=True)
    return lock


def release_lock(lock):
    lock.release()


@shared_task
def process_task(task_id):
    task = Task.objects.get(task_id=task_id)
    session_id = task.session.session_id
    lock = acquire_lock(session_id)  # Prevent multiple runs per session

    try:
        logger.info("Processing %s %s %s",
                    session_id, task.file.path, task.session.app_name)

        current_task.update_state(
            state='PROGRESS',
            meta={'current_process': 'Started Processing File'})

        output = ngspice_helper.ExecXml(task)
        if output == "Streaming":
            state = 'STREAMING'
            current_process = 'Processed Xml, Streaming Output'
        elif output == "Success":
            state = 'SUCCESS'
            current_process = 'Processed Xml, Loading Output'

        current_task.update_state(
            state=state,
            meta={'current_process': current_process})
        return output

    except Exception as e:
        current_task.update_state(state=states.FAILURE, meta={
            'exc_type': type(e).__name__,
            'exc_message': traceback.format_exc().split('\n')})
        logger.exception('Exception Occurred:')
        raise Ignore()

    finally:
        release_lock(lock)  # Ensure lock is always released
