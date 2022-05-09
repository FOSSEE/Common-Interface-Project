import os
import time
import uuid
from celery.utils.log import get_task_logger
from django.http import StreamingHttpResponse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from simulationAPI.models import TaskFile
from simulationAPI.negotiation import IgnoreClientContentNegotiation
from simulationAPI.serializers import TaskSerializer


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
        serializer = TaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            task_id = serializer.data['task_id']
            file_obj = TaskFile.objects.get(task_id=task_id)
            file_obj.log_name = '/tmp/blocks-tmp/scilab-log.txt'
            file_obj.returncode = 0
            file_obj.save()
            response_data = {
                'state': 'PROGRESS',
                'details': serializer.data,
            }
            return Response(response_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

        response_data = {
            'state': 'STREAMING',
            'details': {'current_process': 'Processed Xml, Streaming Output'}
        }
        return Response(response_data)


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


def get_line_and_state(file, figure_list, lineno, incomplete_line):
    '''
    Function to get a new line from file
    This also parses the line and appends new figures to figure List
    '''
    line = file.readline()  # read line by line from log
    if not line:            # if line is empty then return noline
        return (incomplete_line, NOLINE)
    if incomplete_line is not None:
        line = incomplete_line + line
    if '\n' not in line:
        return (line, NOLINE)
    # every line is passed to function parse_line for getting values
    line = line.rstrip()
    (figure_id, state) = parse_line(line, lineno)
    if state == INITIALIZATION:
        # New figure created
        # Add figure ID to list
        figure_list.append(figure_id)  # figure id of block is added to list
        line = None
    elif state == ENDING:
        # End of figure
        # Remove figure ID from list
        # Once ending of log file/data is encountered for that block, figure id
        # will be removed
        figure_list.remove(figure_id)
        line = None
    elif state == NOLINE:
        line = None
    return (line, state)


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
            file_obj = TaskFile.objects.get(task_id=task_id)
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

            while time.time() <= endtime and log_size <= MAX_LOG_SIZE:
                (line, state) = get_line_and_state(log_file, figure_list,
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
                    log_size += len(line)
                    if state == DATA:
                        words = line.split()
                        if len(words) == 15 and words[-1] == 'CSCOPE':
                            interval = starttime + float(words[8]) - time.time() - 0.1
                            if interval > 0:
                                time.sleep(interval)
                        yield "event: log\ndata: %s\n\n" % line
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

        # Notify Client
        yield "event: DONE\ndata: None\n\n"
