import json
from celery.utils.log import get_task_logger
from rest_framework import serializers

from simulationAPI.models import Task, Session

logger = get_task_logger(__name__)


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('session_id', 'app_name', 'created_at')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    session = SessionSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('task_id', 'file', 'parameters', 'upload_time',
                  'log_name', 'returncode', 'task_time', 'session')

    def create(self, validated_data):
        # Takes file from request and stores it along with a taskid
        request = self.context.get('request')
        file = request.FILES.get('file')
        logger.info('File Upload: %s', file)
        post = request.POST
        postdata = post.dict()
        app_name = postdata.pop('app_name')
        session_id = postdata.pop('session_id')
        parameters = json.dumps(postdata, separators=(',', ':'))
        session = Session.objects.create(session_id, app_name)
        task = Task.objects.create(
            session=session, file=file, parameters=parameters)
        logger.info('session: %s, task: %s', session, task)
        return task
