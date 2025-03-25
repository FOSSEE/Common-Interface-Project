from celery.utils.log import get_task_logger
import json
from rest_framework import serializers

from simulationAPI.models import Task, Session

logger = get_task_logger(__name__)


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

        file_extension = file.name.split('.')[-1].lower()
        if file_extension not in ['xml', 'sce']:
            raise serializers.ValidationError({"file": "Invalid file type. Only .xml and .sce files are allowed."})
        
        session_id = request.headers.get("Session-ID")

        post = request.POST
        postdata = post.dict()
        app_name = postdata.pop('app_name')
        type = postdata.pop('type', 'XCOS')
        parameters = json.dumps(postdata, separators=(',', ':'))
        session, created = Session.objects.get_or_create(session_id=session_id, app_name=app_name)
        task = Task.objects.create(session=session, file=file, type=type, parameters=parameters)
        logger.info("Session: %s (created: %s), Task: %s", session, created, task)
        return task
