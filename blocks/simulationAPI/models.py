from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import uuid


class Task(models.Model):
    task_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    task_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        """String for representing the Model object."""
        return self.task_id.hex


class TaskFile(models.Model):
    file_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT))
    app_name = models.CharField(max_length=100, blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    upload_time = models.DateTimeField(auto_now=True)
    log_name = models.CharField(max_length=500, blank=True, null=True)
    returncode = models.IntegerField(blank=True, null=True)
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='file')

    def save(self, *args, **kwargs):
        super(TaskFile, self).save(*args, **kwargs)

    def __str__(self):
        """String for representing the Model object."""
        return self.file_id.hex
