from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import uuid


# For handling file uploads to a permenant direcrory
file_storage = FileSystemStorage(
    location=settings.FILE_STORAGE_ROOT, base_url=settings.FILE_STORAGE_URL)

media = FileSystemStorage(
    location=settings.MEDIA_ROOT, base_url='.')


class BookCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=500)

    def __str__(self):
        return self.category_name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=500)
    author_name = models.CharField(max_length=500)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name


class StateSave(models.Model):
    id = models.AutoField(primary_key=True)
    save_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=100, default="Untitled")
    description = models.CharField(max_length=400, null=True)
    shared = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    save_time = models.DateTimeField(auto_now=True, db_index=True)
    owner = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    data_dump = models.TextField(null=False)
    base64_image = models.ImageField(
        upload_to='simulation_images', storage=file_storage, null=True)

    def save(self, *args, **kwargs):
        super(StateSave, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    save_id = models.CharField(unique=True, max_length=50, null=False)
    name = models.CharField(max_length=100, default="Untitled")
    description = models.CharField(max_length=400, null=True)
    save_time = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, related_name='examples', on_delete=models.CASCADE, null=True)
    data_dump = models.TextField(null=False)
    media = models.CharField(max_length=100, null=False)

    # For Django Admin Panel
    def image_tag(self):
        if self.media:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />',
                               mark_safe(self.media.url))
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name
