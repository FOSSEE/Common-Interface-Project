from celery.result import AsyncResult
from celery.utils.log import get_task_logger
from django.conf import settings
from django.http import StreamingHttpResponse, JsonResponse
import os
import time
import uuid
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blocks.celery_tasks import app
from simulationAPI.models import Task, Session
from simulationAPI.negotiation import IgnoreClientContentNegotiation
from simulationAPI.serializers import TaskSerializer
from simulationAPI.tasks import process_task, process_task_script
from simulationAPI.helpers.ngspice_helper import CreateXcos, update_task_status



SCILAB_INSTANCE_TIMEOUT_INTERVAL = 300
MAX_LOG_SIZE = 512 * 1024
LOOK_DELAY = 0.1

# States of the line
# to indicate initialization of block in log file is encountered
INITIALIZATION = 0
# to indicate ending of log file data for that block is encountered
ENDING = 1
# to indicate data is proper and can be read
DATA = 2
# to indicate there is no line in log file further
NOLINE = -1

logger = get_task_logger(__name__)


class XmlUploader(APIView):
    '''
    API for XmlUpload

    Requires a multipart/form-data POST Request with Xml file in the
    'file' parameter
    '''
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        logger.info('Got POST for Xml upload: data=%s', request.data)

        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        file_extension = uploaded_file.name.split('.')[-1].lower()

        # Validate file type
        if file_extension not in ['xml', 'sce']:
            return Response({"error": "Invalid file type. Only .xml and .sce files are allowed."},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = TaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            task = serializer.save()

            task_type = request.data.get('type')
            script_task_id = request.data.get('script_task_id')

            if task_type == 'XCOS' and script_task_id:
                try:
                    script_task = Task.objects.get(task_id=script_task_id, type='SCRIPT')
                    if script_task.workspace_file:
                        task.workspace_file = script_task.workspace_file
                        task.save()
                        logger.info(f'Copied workspace file from script task {script_task_id} to xcos task {task.task_id}')
                    else:
                        logger.warning(f'Script task {script_task_id} does not have a workspace file')
                except Task.DoesNotExist:
                    logger.warning(f'Script task {script_task_id} not found')
            # serializer.save()
            task_id = serializer.data['task_id']
            celery_task = process_task.apply_async(
                kwargs={'task_id': str(task_id)}, task_id=str(task_id))
            response_data = {
                'state': celery_task.state,
                'details': serializer.data,
            }
            return Response(response_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class XmlSave(APIView):
    '''
    API for XmlSave

    Requires a multipart/form-data POST Request with Xml file in the
    'file' parameter
    '''
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        logger.info('Got POST for Xml save: data=%s', request.data)
        file = request.FILES.get('file', None)
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
        file_name = file.name
        file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file_name)

        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        try:
            # Update the request data to include the file path
            data = request.data.copy()
            data['file_path'] = file_path
            filename = CreateXcos(data['file_path'], '{}', 'saves')
            with open(filename, 'r') as file:
                filecontent = file.read()

            response = Response(filecontent, status=status.HTTP_200_OK,
                                content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(filename)}"'
            return response
        except Exception as e:
            logger.error('Error while creating Xcos file: %s', str(e))
            return Response({"error": "Error while creating Xcos file"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CeleryResultView(APIView):
    """

    Returns Simulation results for 'task_id' provided after
    uploading the xml
    /api/task/<uuid>

    """
    permission_classes = (AllowAny,)
    methods = ['GET']

    def get(self, request, task_id):
        if not isinstance(task_id, uuid.UUID):
            raise ValidationError('Invalid uuid format')
        task_id = str(task_id)

        celery_result = AsyncResult(task_id)
        response_data = {
            'task_id': task_id,
            'state': celery_result.state,
            'details': str(celery_result.info)
        }
        return Response(response_data)


class CancelTaskView(APIView):
    """Cancels a running Celery task."""
    permission_classes = (AllowAny,)
    methods = ['GET']

    def get(self, request, task_id):
        """Handles task cancellation request."""
        if not isinstance(task_id, uuid.UUID):
            raise ValidationError('Invalid uuid format')
        task_id = str(task_id)

        # Cancel the task
        app.control.revoke(task_id, terminate=True)

        # Check if task was actually revoked
        celery_result = AsyncResult(task_id)
        response_data = {
            'task_id': task_id,
            'state': celery_result.state,
            'details': str(celery_result.info)
        }

        return Response(response_data, status=status.HTTP_200_OK)


def parse_line(line, lineno):
    '''
    Function to parse the line
    Returns tuple of figure ID and state
    state = INITIALIZATION if new figure is created
            ENDING if current fig end
            DATA otherwise
    '''
    line_words = line.split(' ')  # Each line is split to read condition
    try:
        # The below condition determines the block ID
        if line_words[0] == "Initialization":
            # New figure created
            # Get fig id
            # to extract figure ids (sometime multiple sinks can be used in one
            # diagram to differentiate that)
            figure_id = line_words[-1]
            state = INITIALIZATION
        elif line_words[0] == "Ending":
            # Current figure end
            # Get fig id
            figure_id = line_words[-1]
            state = ENDING
        else:
            # Current figure coordinates
            figure_id = line_words[2]
            state = DATA
        return (figure_id, state)
    except Exception as e:
        logger.error('%s while parsing %s on line %s', str(e), line, lineno)
        return (None, NOLINE)


def get_line_and_state(file, figure_list, lastlogtimes,
                       lineno, incomplete_line):
    '''
    Function to get a new line from file
    This also parses the line and appends new figures to figure List
    '''
    line = file.readline()  # read line by line from log
    if not line:            # if line is empty then return noline
        return (incomplete_line, None, NOLINE)
    if incomplete_line is not None:
        line = incomplete_line + line
    if '\n' not in line:
        return (line, None, NOLINE)
    # every line is passed to function parse_line for getting values
    line = line.rstrip()
    (figure_id, state) = parse_line(line, lineno)
    if state == INITIALIZATION:
        # New figure created
        # Add figure ID to list
        figure_list.append(figure_id)  # figure id of block is added to list
        lastlogtimes[figure_id] = -1
        line = None
    elif state == ENDING:
        # End of figure
        # Remove figure ID from list
        # Once ending of log file/data is encountered for that block, figure id
        # will be removed
        figure_list.remove(figure_id)
        del lastlogtimes[figure_id]
        line = None
    elif state == NOLINE:
        line = None
    return (line, figure_id, state)


class StreamView(APIView):
    """

    Streams Simulation results for 'task_id' provided after
    uploading the xml
    /api/streaming/<uuid>

    """
    permission_classes = (AllowAny,)
    methods = ['GET']
    content_negotiation_class = IgnoreClientContentNegotiation

    def get(self, request, task_id):
        return StreamingHttpResponse(self.event_stream(task_id), content_type='text/event-stream')

    def get_log_name(self, task_id):
        while True:
            file_obj = Task.objects.get(task_id=task_id)
            log_name = file_obj.log_name
            returncode = file_obj.returncode
            if log_name is None:
                if returncode is None:
                    time.sleep(LOOK_DELAY)
                    continue
                logger.warning('log_name is None')
                return None
            if not os.path.isfile(log_name):
                logger.warning('log file does not exist')
                return None
            if os.stat(log_name).st_size == 0:
                if returncode is None:
                    time.sleep(LOOK_DELAY)
                    continue
                logger.warning('log file is empty')
                return None
            return log_name

    def handle_duplicate_lines(self):
        if self.duplicatelineno == 0:
            return

        self.duplicatelines += self.duplicatelineno
        yield "event: duplicate\ndata: %d\n\n" % self.duplicatelineno
        self.duplicatelineno = 0

    def event_stream(self, task_id):
        if not isinstance(task_id, uuid.UUID):
            raise ValidationError('Invalid uuid format')

        log_name = self.get_log_name(task_id)
        if log_name is None:
            yield "event: ERROR\ndata: no log file found\n\n"
            return

        with open(log_name, 'r') as log_file:
            # Start sending log
            self.duplicatelineno = 0
            self.duplicatelines = 0
            lastline = ''
            lineno = 0
            line = None
            starttime = time.time()
            endtime = starttime + SCILAB_INSTANCE_TIMEOUT_INTERVAL
            log_size = 0
            figure_list = []
            lastlogtimes = {}

            while time.time() <= endtime and log_size <= MAX_LOG_SIZE:
                (line, figure_id, state) = get_line_and_state(log_file, figure_list, lastlogtimes,
                                                              lineno, line)
                # if incomplete line, wait for the complete line
                if state == NOLINE:
                    time.sleep(LOOK_DELAY)
                    continue

                if not figure_list:
                    break
                # Get the line and loop until the state is ENDING and figure_list
                # empty. Determine if we get block id and give it to chart.js
                if line is None:
                    continue
                if lastline != line:
                    self.handle_duplicate_lines()
                    lastline = line
                    if state == DATA:
                        words = line.split()
                        if len(words) == 15 and words[-1] == 'CSCOPE':
                            logtime = float(words[8])
                            totallogtime = float(words[-2])
                            if logtime < lastlogtimes[figure_id] + 0.001 * totallogtime:
                                line = None
                                continue
                            lastlogtimes[figure_id] = logtime
                            interval = starttime + logtime - time.time() - 0.1
                            if interval > 0:
                                time.sleep(interval)
                        send_line = "event: log\ndata: %s\n\n" % line
                        log_size += len(send_line)
                        yield send_line
                else:
                    self.duplicatelineno += 1
                lineno += 1
                line = None

            self.handle_duplicate_lines()

            if self.duplicatelines != 0:
                logger.info('lines = %s, duplicate lines = %s, log size = %s',
                            lineno, self.duplicatelines, log_size)
            else:
                logger.info('lines = %s, log size = %s', lineno, log_size)

        update_task_status(task_id, 'SUCCESS')
        # Notify Client
        yield "event: DONE\ndata: None\n\n"


class GetScriptOutputView(APIView):
    """
    API endpoint to get the output of a script execution.
    """

    def get(self, request, task_id, *args, **kwargs):

        try:
            celery_task = process_task_script.apply_async(kwargs={'task_id': str(task_id)}, task_id=str(uuid.uuid4()))
            result = celery_task.get(timeout=30)
            update_task_status(celery_task.id, 'SUCCESS', meta=result)
            print("RESULT:", result)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error calling getscriptoutput (Task_id: {task_id}): {str(e)}")
            return Response({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_session(request):
    if not request.session.session_key:
        request.session.save()  # Create a new session if not already exists

    session_id = request.session.session_key
    app_name = request.GET.get('app_name', None)

    # Save or update session in the custom table
    session, created = Session.objects.update_or_create(
        session_id=session_id,
        app_name=app_name
    )

    return JsonResponse({'session_id': session_id, 'expire_at': session.expire_at})
