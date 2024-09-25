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
    parameters = serializers.ListField(
        child=serializers.CharField(max_length=100, required=False,
                                    allow_blank=True, trim_whitespace=True),
        required=True
    )

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
