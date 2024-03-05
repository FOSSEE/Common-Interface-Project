from rest_framework import serializers

from .models import BlockType, Category, ParameterDataType, BlockPrefix, \
    BlockPrefixParameter, Block, BlockParameter, BlockPort, \
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


class BlockPrefixParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockPrefixParameter
        fields = [
            'id',
            'blockprefix',
        ]


class BlockPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockPort
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


class BlockSerializer(serializers.ModelSerializer):
    blockprefix = BlockPrefixSerializer()
    main_category = CategorySerializer()
    categories = CategorySerializer(many=True)
    blockport_set = BlockPortSerializer(many=True)

    class Meta:
        model = Block
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
            'p000_value_initial',
            'p001_value_initial',
            'p002_value_initial',
            'p003_value_initial',
            'p004_value_initial',
            'p005_value_initial',
            'p006_value_initial',
            'p007_value_initial',
            'p008_value_initial',
            'p009_value_initial',
            'p010_value_initial',
            'p011_value_initial',
            'p012_value_initial',
            'p013_value_initial',
            'p014_value_initial',
            'p015_value_initial',
            'p016_value_initial',
            'p017_value_initial',
            'p018_value_initial',
            'p019_value_initial',
            'p020_value_initial',
            'p021_value_initial',
            'p022_value_initial',
            'p023_value_initial',
            'p024_value_initial',
            'p025_value_initial',
            'p026_value_initial',
            'p027_value_initial',
            'p028_value_initial',
            'p029_value_initial',
            'p030_value_initial',
            'p031_value_initial',
            'p032_value_initial',
            'p033_value_initial',
            'p034_value_initial',
            'p035_value_initial',
            'p036_value_initial',
            'p037_value_initial',
            'p038_value_initial',
            'p039_value_initial',
            'p040_value_initial',
            'p041_value_initial',
            'p042_value_initial',
            'p043_value_initial',
            'p044_value_initial',
            'p045_value_initial',
            'p046_value_initial',
            'p047_value_initial',
            'p048_value_initial',
            'p049_value_initial',
            'p050_value_initial',
            'p051_value_initial',
            'p052_value_initial',
            'p053_value_initial',
            'p054_value_initial',
            'p055_value_initial',
            'p056_value_initial',
            'p057_value_initial',
            'p058_value_initial',
            'p059_value_initial',
            'blockport_set',
        ]

    @staticmethod
    def prefetch_category(queryset):
        return queryset.prefetch_related('categories')

    @staticmethod
    def prefetch_blockport(queryset):
        return queryset.prefetch_related('blockport_set')


class BlockParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockParameter
        fields = [
            'id',
            'block',
            'p000',
            'p000_type',
            'p000_help',
            'p001',
            'p001_type',
            'p001_help',
            'p002',
            'p002_type',
            'p002_help',
            'p003',
            'p003_type',
            'p003_help',
            'p004',
            'p004_type',
            'p004_help',
            'p005',
            'p005_type',
            'p005_help',
            'p006',
            'p006_type',
            'p006_help',
            'p007',
            'p007_type',
            'p007_help',
            'p008',
            'p008_type',
            'p008_help',
            'p009',
            'p009_type',
            'p009_help',
            'p010',
            'p010_type',
            'p010_help',
            'p011',
            'p011_type',
            'p011_help',
            'p012',
            'p012_type',
            'p012_help',
            'p013',
            'p013_type',
            'p013_help',
            'p014',
            'p014_type',
            'p014_help',
            'p015',
            'p015_type',
            'p015_help',
            'p016',
            'p016_type',
            'p016_help',
            'p017',
            'p017_type',
            'p017_help',
            'p018',
            'p018_type',
            'p018_help',
            'p019',
            'p019_type',
            'p019_help',
            'p020',
            'p020_type',
            'p020_help',
            'p021',
            'p021_type',
            'p021_help',
            'p022',
            'p022_type',
            'p022_help',
            'p023',
            'p023_type',
            'p023_help',
            'p024',
            'p024_type',
            'p024_help',
            'p025',
            'p025_type',
            'p025_help',
            'p026',
            'p026_type',
            'p026_help',
            'p027',
            'p027_type',
            'p027_help',
            'p028',
            'p028_type',
            'p028_help',
            'p029',
            'p029_type',
            'p029_help',
            'p030',
            'p030_type',
            'p030_help',
            'p031',
            'p031_type',
            'p031_help',
            'p032',
            'p032_type',
            'p032_help',
            'p033',
            'p033_type',
            'p033_help',
            'p034',
            'p034_type',
            'p034_help',
            'p035',
            'p035_type',
            'p035_help',
            'p036',
            'p036_type',
            'p036_help',
            'p037',
            'p037_type',
            'p037_help',
            'p038',
            'p038_type',
            'p038_help',
            'p039',
            'p039_type',
            'p039_help',
            'p040',
            'p040_type',
            'p040_help',
            'p041',
            'p041_type',
            'p041_help',
            'p042',
            'p042_type',
            'p042_help',
            'p043',
            'p043_type',
            'p043_help',
            'p044',
            'p044_type',
            'p044_help',
            'p045',
            'p045_type',
            'p045_help',
            'p046',
            'p046_type',
            'p046_help',
            'p047',
            'p047_type',
            'p047_help',
            'p048',
            'p048_type',
            'p048_help',
            'p049',
            'p049_type',
            'p049_help',
            'p050',
            'p050_type',
            'p050_help',
            'p051',
            'p051_type',
            'p051_help',
            'p052',
            'p052_type',
            'p052_help',
            'p053',
            'p053_type',
            'p053_help',
            'p054',
            'p054_type',
            'p054_help',
            'p055',
            'p055_type',
            'p055_help',
            'p056',
            'p056_type',
            'p056_help',
            'p057',
            'p057_type',
            'p057_help',
            'p058',
            'p058_type',
            'p058_help',
            'p059',
            'p059_type',
            'p059_help',
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
            'p_order',
            'p_value_initial',
        ]


class NewBlockParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBlockParameter
        fields = [
            'p_order',
            'p_label',
            'p_type',
            'p_help',
        ]


class NewBlockSerializer(serializers.ModelSerializer):
    blockprefix = BlockPrefixSerializer()
    main_category = CategorySerializer()
    categories = CategorySerializer(many=True)
    newblockport_set = NewBlockPortSerializer(many=True)
    newblockparameter_set = NewBlockParameterValueSerializer(many=True)

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
            'newblockport_set',
            'newblockparameter_set',
        ]

    @staticmethod
    def prefetch_category(queryset):
        return queryset.prefetch_related('categories')

    @staticmethod
    def prefetch_blockport(queryset):
        return queryset.prefetch_related('newblockport_set')

    @staticmethod
    def prefetch_blockparameter(queryset):
        return queryset.prefetch_related('newblockparameter_set')


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
