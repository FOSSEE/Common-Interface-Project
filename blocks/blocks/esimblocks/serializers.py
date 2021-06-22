from rest_framework import serializers

from .models import Category, ParameterDataType, BlockType, BlockPrefix, \
    Block, BlockParameter, BlockPort


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
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


class BlockTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockType
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
    blockport_set = BlockPortSerializer(many=True)

    class Meta:
        model = Block
        fields = [
            'id',
            'blocktype',
            'name',
            'blockprefix',
            'main_category',
            'categories',
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
            'p001',
            'p001_type',
            'p002',
            'p002_type',
            'p003',
            'p003_type',
            'p004',
            'p004_type',
            'p005',
            'p005_type',
            'p006',
            'p006_type',
            'p007',
            'p007_type',
            'p008',
            'p008_type',
            'p009',
            'p009_type',
            'p010',
            'p010_type',
            'p011',
            'p011_type',
            'p012',
            'p012_type',
            'p013',
            'p013_type',
            'p014',
            'p014_type',
            'p015',
            'p015_type',
            'p016',
            'p016_type',
            'p017',
            'p017_type',
            'p018',
            'p018_type',
            'p019',
            'p019_type',
            'p020',
            'p020_type',
            'p021',
            'p021_type',
            'p022',
            'p022_type',
            'p023',
            'p023_type',
            'p024',
            'p024_type',
            'p025',
            'p025_type',
            'p026',
            'p026_type',
            'p027',
            'p027_type',
            'p028',
            'p028_type',
            'p029',
            'p029_type',
            'p030',
            'p030_type',
            'p031',
            'p031_type',
            'p032',
            'p032_type',
            'p033',
            'p033_type',
            'p034',
            'p034_type',
            'p035',
            'p035_type',
            'p036',
            'p036_type',
            'p037',
            'p037_type',
            'p038',
            'p038_type',
            'p039',
            'p039_type',
        ]


class ErrorSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    error = serializers.CharField(
        max_length=200, allow_blank=False, trim_whitespace=True)


class SetBlockParameterSerializer(serializers.Serializer):
    block_id = serializers.IntegerField()
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
        blockports = BlockPort.objects.filter(block=self.data['block_id'])
        number_of_blockports = len(blockports)

        # TODO: change values depending on block name

        return SetBlockPortSerializer(data={
            'number_of_blockports': number_of_blockports
        })


class SetBlockPortSerializer(serializers.Serializer):
    number_of_blockports = serializers.IntegerField()
