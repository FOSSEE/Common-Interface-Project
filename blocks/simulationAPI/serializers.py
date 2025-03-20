import json
import logging
from rest_framework import serializers

from simulationAPI.models import Task, Session

logger = logging.getLogger("celery")


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('session_id', 'app_name', 'created_at', 'expire_at', 'count')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    session = SessionSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('task_id', 'file', 'type', 'status',
                  'parameters', 'upload_time', 'log_name', 'workspace_file',
                  'returncode', 'session', 'start_time', 'end_time')

    def create(self, validated_data):
        # Takes file from request and stores it along with a taskid
        request = self.context.get('request')
        file = request.FILES.get('file')
        logger.info('File Upload: %s', file)

        session_id = request.headers.get("Session-ID")

        post = request.POST
        postdata = post.dict()
        app_name = postdata.pop('app_name')
        parameters = json.dumps(postdata, separators=(',', ':'))
        session, created = Session.objects.get_or_create(session_id=session_id, app_name=app_name)
        task = Task.objects.create(session=session, file=file, parameters=parameters)
        logger.info("Session: %s (created: %s), Task: %s", session, created, task)
        return task
