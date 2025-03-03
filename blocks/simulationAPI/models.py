from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
import uuid


# session
class Session(models.Model):
    session_id = models.CharField(primary_key=True, max_length=40, null=False, editable=False)
    app_name = models.CharField(max_length=40, blank=False, null=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField(default=timezone.now() + timedelta(days=1))
    count = models.IntegerField(null=False, default=0)

    def save(self, *args, **kwargs):
        if self.pk is None:  # New entry
            self.count = 1
            super().save(*args, **kwargs)
            return

        old_instances = Session.objects.filter(pk=self.pk)
        if not old_instances.exists():  # New entry
            self.count = 1
            super().save(*args, **kwargs)
            return

        old_instance = old_instances.first()
        if old_instance.app_name == self.app_name:
            self.count += 1
            kwargs['update_fields'] = ['count']
            super().save(*args, **kwargs)
            return

        raise ValidationError("mismatch: Cannot update app name.")

    def __str__(self):
        return self.session_id


class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), default='default_file.txt')

    parameters = models.TextField(blank=True, null=True)
    upload_time = models.DateTimeField(auto_now=True)
    log_name = models.CharField(max_length=500, blank=True, null=True)
    returncode = models.IntegerField(blank=True, null=True)

    task_time = models.DateTimeField(auto_now=True)

    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='task_files', null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        """String for representing the Model object."""
        return self.task_id.hex
