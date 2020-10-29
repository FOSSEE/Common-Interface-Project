from celery import shared_task, current_task
from celery import states
from simulationAPI.helpers import ngspice_helper
from celery.exceptions import Ignore
import traceback
from simulationAPI.models import TaskFile
import logging


logger = logging.getLogger(__name__)


@shared_task
def process_task(task_id):
    try:

        task_filter = TaskFile.objects.filter(task_id=task_id)
        file_obj = list(task_filter)[0]
        file_path = file_obj.file.path
        file_id = file_obj.file_id

        logger.info("Processing %s %s", file_path, file_id)

        current_task.update_state(
            state='PROGRESS',
            meta={'current_process': 'Started Processing File'})

        output = ngspice_helper.ExecXml(file_path, file_id)
        current_task.update_state(
            state='PROGRESS',
            meta={'current_process': 'Processed Xml, Loading Output'})
        return output

    except Exception as e:
        current_task.update_state(state=states.FAILURE, meta={
            'exc_type': type(e).__name__,
            'exc_message': traceback.format_exc().split('\n')})
        logger.warning('Exception Occurred: %s', str(e))
        raise Ignore()
