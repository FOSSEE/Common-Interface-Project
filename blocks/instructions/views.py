import time
from celery.utils.log import get_task_logger
from django.http import StreamingHttpResponse
from random import randrange
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from simulationAPI.negotiation import IgnoreClientContentNegotiation


logger = get_task_logger(__name__)


class Instructions(APIView):
    """
    Streams instructions

    """
    permission_classes = (AllowAny,)
    methods = ['GET']
    content_negotiation_class = IgnoreClientContentNegotiation

    def get(self, request):
        return StreamingHttpResponse(self.event_stream(), content_type='text/event-stream')

    def event_stream(self):
        done = False
        while not done:
            number = randrange(100)
            sleep = randrange(1, 4)
            if number < 75:
                event = 'instruction'
                data = 'add'
            elif number < 90:
                event = 'instruction'
                data = 'remove'
            elif number < 99:
                event = 'instruction'
                data = 'reset'
            else:
                event = 'done'
                data = 'None'
                done = True

            # Notify Client
            yield 'event: %s\ndata: %s\n\n' % (event, data)

            if done:
                return

            time.sleep(sleep)
