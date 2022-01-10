import traceback
from celery import shared_task, current_task, states
from celery.exceptions import Ignore
from celery.utils.log import get_task_logger

from simulationAPI.helpers import ngspice_helper
from simulationAPI.models import TaskFile


logger = get_task_logger(__name__)


@shared_task
def process_task(task_id):
    try:
        file_obj = TaskFile.objects.get(task_id=task_id)

        logger.info("Processing %s %s %s",
                    file_obj.file.path, file_obj.file_id, file_obj.app_name)

        current_task.update_state(
            state='PROGRESS',
            meta={'current_process': 'Started Processing File'})

        output = ngspice_helper.ExecXml(file_obj)
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
