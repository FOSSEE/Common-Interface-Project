import time
from celery.utils.log import get_task_logger
from django.http import StreamingHttpResponse
from random import choice, randrange
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
        allChartIds = []
        allIdDicts = {}
        resets = 0
        while not done:
            number = randrange(100)
            sleep = randrange(0, 3)
            if number < 100 - 30 * (1 + resets) * len(allChartIds):
                chartId = randrange(100)
                while chartId in allIdDicts:
                    chartId = randrange(100)
                chartType = choice(['area', 'line', 'spline'])
                xMin = randrange(-10, 10)
                xMax = xMin + randrange(10, 20)
                yMin = randrange(-10, 10)
                yMax = yMin + randrange(10, 20)
                idDict = {'chartType': chartType,
                          'xMin': xMin, 'yMin': yMin, 'xMax': xMax, 'yMax': yMax, 'xNext': xMin}
                allChartIds.append(chartId)
                allIdDicts[chartId] = idDict
                event = 'instruction'
                data = 'addChart id=%s type=%s xMin=%s xMax=%s yMin=%s yMax=%s' % (
                        chartId, chartType, xMin, xMax, yMin, yMax)
            elif number < 100 - 2 * (1 + resets) * len(allChartIds):
                chartId = choice(allChartIds)
                idDict = allIdDicts[chartId]
                x = idDict['xNext']
                y = randrange(idDict['yMin'], idDict['yMax'])
                idDict['xNext'] = x + 1
                event = 'instruction'
                data = 'addData id=%s x=%s y=%s' % (chartId, x, y)
            elif number < 100 - (1 + resets) * len(allChartIds):
                print('reset:', allIdDicts)
                allChartIds.clear()
                allIdDicts.clear()
                resets += 1
                event = 'instruction'
                data = 'reset'
            else:
                print('done:', allIdDicts)
                done = True
                event = 'done'
                data = 'none'

            # Notify Client
            yield 'event: %s\ndata: %s\n\n' % (event, data)

            if done:
                return

            time.sleep(sleep)
