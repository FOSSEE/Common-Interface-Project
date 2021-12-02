import json
import logging
from rest_framework import serializers
from simulationAPI.models import TaskFile, Task

logger = logging.getLogger(__name__)


class TaskFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskFile
        fields = ('file_id', 'file', 'app_name', 'parameters', 'upload_time',
                  'log_name', 'returncode', 'task')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    file = TaskFileSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('task_id', 'task_time', 'file')

    def create(self, validated_data):
        # Takes file from request and stores it along with a taskid
        request = self.context.get('request')
        file = request.FILES.get('file')
        logger.info('File Upload: %s', file)
        post = request.POST
        postdata = post.dict()
        app_name = postdata.pop('app_name')
        parameters = json.dumps(postdata, separators=(',', ':'))
        task = Task.objects.create()
        taskfile = TaskFile.objects.create(
            task=task, file=file, app_name=app_name, parameters=parameters)
        logger.info('task: %s, taskfile: %s', task, taskfile)
        return task
