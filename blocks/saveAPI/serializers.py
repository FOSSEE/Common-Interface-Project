from rest_framework import serializers
from saveAPI.models import StateSave, Gallery
from django.core.files.base import ContentFile
import base64
import six
import uuid
import imghdr


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        _, data = self.update(data)
        return super(Base64ImageField, self).to_internal_value(data)

    def update(self, data):
        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')
        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            self.fail('invalid_image')
        file_name = str(uuid.uuid4())
        file_extension = imghdr.what(file_name, decoded_file)
        complete_file_name = "%s.%s" % (file_name, file_extension,)
        data = ContentFile(decoded_file, name=complete_file_name)
        return complete_file_name, data


class StateSaveSerializer(serializers.ModelSerializer):
    base64_image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = StateSave
        fields = ('id',
                  'name',
                  'description',
                  'save_time',
                  'create_time',
                  'save_id',
                  'data_dump',
                  'shared',
                  'owner',
                  'base64_image',
                  )


class SaveListSerializer(serializers.ModelSerializer):
    base64_image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = StateSave
        fields = ('id',
                  'name',
                  'description',
                  'save_time',
                  'create_time',
                  'save_id',
                  'shared',
                  'base64_image',
                  )


class GallerySerializer(serializers.ModelSerializer):
    media = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Gallery
        fields = ('save_id',
                  'data_dump',
                  'name',
                  'description',
                  'media',
                  'shared',
                  )
