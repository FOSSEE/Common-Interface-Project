from celery import shared_task, states
from celery.exceptions import Ignore
from redis import Redis
import traceback

from blocks.celery_tasks import app
from simulationAPI.helpers.ngspice_helper import ExecXml, update_task_status
from simulationAPI.logging_utils import get_task_logger_adapter as get_task_logger
from simulationAPI.models import Task

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
    logger.extra = {'task_name': self.name, 'task_id': self.request.id}
    task = Task.objects.get(task_id=task_id)
    session_id = task.session.session_id
    lock = acquire_lock(session_id)  # Prevent multiple runs per session

    try:
        logger.info("Processing %s %s %s",
                    session_id, task.file.path, task.session.app_name)

        update_task_status(task_id, 'STARTED',
                           meta={'current_process': 'Started Processing File'})

        output = ExecXml(task, self.name)
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
