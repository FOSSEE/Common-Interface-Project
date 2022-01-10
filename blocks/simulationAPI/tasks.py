import json
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
        file_path = file_obj.file.path
        file_id = file_obj.file_id
        app_name = file_obj.app_name
        parameters = json.loads(file_obj.parameters)

        logger.info("Processing %s %s %s", file_path, file_id, app_name)

        current_task.update_state(
            state='PROGRESS',
            meta={'current_process': 'Started Processing File'})

        output = ngspice_helper.ExecXml(file_path, file_id, parameters)
        if output[0] == "Streaming":
            file_obj.log_name = output[1]
            file_obj.returncode = output[2]
            file_obj.save()
            state = 'STREAMING'
            current_process = 'Processed Xml, Streaming Output'
        elif output[0] == "Success":
            state = 'SUCCESS'
            current_process = 'Processed Xml, Loading Output'
        current_task.update_state(
            state=state,
            meta={'current_process': current_process})
        return output[0]

    except Exception as e:
        current_task.update_state(state=states.FAILURE, meta={
            'exc_type': type(e).__name__,
            'exc_message': traceback.format_exc().split('\n')})
        logger.exception('Exception Occurred:')
        raise Ignore()
