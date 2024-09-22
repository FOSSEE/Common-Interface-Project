from rest_framework import serializers
from django.db.models import Prefetch

from .models import BlockType, Category, ParameterDataType, BlockPrefix, \
    NewBlock, NewBlockParameter, NewBlockPort

from .xcosblocks import *


class BlockTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockType
        fields = [
            'id',
            'name',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'blocktype',
            'name',
            'sort_order',
        ]


class ParameterDataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParameterDataType
        fields = [
            'id',
            'name',
        ]


class BlockPrefixSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockPrefix
        fields = [
            'id',
            'name',
        ]


class ErrorSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    error = serializers.CharField(
        max_length=200, allow_blank=False, trim_whitespace=True)


class SetBlockParameterSerializer(serializers.Serializer):
    block = serializers.CharField(max_length=100, required=True,
                                  allow_blank=False, trim_whitespace=True)
    p000_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p001_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p002_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p003_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p004_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p005_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p006_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p007_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p008_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p009_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p010_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p011_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p012_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p013_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p014_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p015_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p016_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p017_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p018_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p019_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p020_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p021_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p022_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p023_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p024_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p025_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p026_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p027_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p028_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p029_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p030_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p031_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p032_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p033_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p034_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p035_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p036_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p037_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p038_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)
    p039_value = serializers.CharField(max_length=100, required=False,
                                       allow_blank=True, trim_whitespace=True)

    def getblockportserializer(self):
        data = self.data
        name = data['block']

        (parameters, display_parameter, ports) = \
            globals()['get_from_' + name](data)
        simulation_function = ''

        return SetBlockPortSerializer(data={
            'parameters': parameters,
            'display_parameter': display_parameter,
            'simulation_function': simulation_function,
            'ports': ports,
        })


class SetBlockPortSerializer(serializers.Serializer):
    parameters = serializers.StringRelatedField(many=True)
    display_parameter = serializers.CharField(
        max_length=100, allow_blank=True, trim_whitespace=True)
    simulation_function = serializers.CharField(
        max_length=100, allow_blank=True, trim_whitespace=True)
    ports = serializers.StringRelatedField(many=True)


class NewBlockPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBlockPort
        fields = [
            'id',
            'block',
            'port_order',
            'port_name',
            'port_number',
            'port_x',
            'port_y',
            'port_orientation',
            'port_part',
            'port_dmg',
            'port_type',
        ]


class NewBlockParameterValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBlockParameter
        fields = [
            'p_value_initial',
        ]


class NewBlockParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBlockParameter
        fields = [
            'p_label',
            'p_type',
            'p_help',
        ]


class NewBlockSerializer(serializers.ModelSerializer):
    blockprefix = BlockPrefixSerializer()
    main_category = CategorySerializer()
    categories = CategorySerializer(many=True)
    newblockparameter_set = NewBlockParameterValueSerializer(many=True)
    newblockport_set = NewBlockPortSerializer(many=True)

    class Meta:
        model = NewBlock
        fields = [
            'id',
            'name',
            'blockprefix',
            'main_category',
            'categories',
            'block_name',
            'initial_display_parameter',
            'simulation_function',
            'block_image_path',
            'block_width',
            'block_height',
            'newblockparameter_set',
            'newblockport_set',
        ]

    @staticmethod
    def prefetch_category(queryset):
        return queryset.prefetch_related('categories')

    @staticmethod
    def prefetch_blockparameter(queryset):
        return queryset.prefetch_related(Prefetch(
            'newblockparameter_set',
            NewBlockParameter.objects.order_by('block_id', 'p_order')))

    @staticmethod
    def prefetch_blockport(queryset):
        return queryset.prefetch_related('newblockport_set')


class SetNewBlockParameterSerializer(serializers.Serializer):
    block = serializers.CharField(max_length=100, required=True,
                                  allow_blank=False, trim_whitespace=True)

    def getblockportserializer(self):
        data = self.data
        name = data['block']

        (parameters, display_parameter, ports) = \
            globals()['get_from_' + name](data)
        simulation_function = ''

        return SetNewBlockPortSerializer(data={
            'parameters': parameters,
            'display_parameter': display_parameter,
            'simulation_function': simulation_function,
            'ports': ports,
        })


class SetNewBlockPortSerializer(serializers.Serializer):
    parameters = serializers.StringRelatedField(many=True)
    display_parameter = serializers.CharField(
        max_length=100, allow_blank=True, trim_whitespace=True)
    simulation_function = serializers.CharField(
        max_length=100, allow_blank=True, trim_whitespace=True)
    ports = serializers.StringRelatedField(many=True)
