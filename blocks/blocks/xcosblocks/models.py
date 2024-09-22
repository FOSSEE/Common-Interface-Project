from django.db import models


class BlockType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    blocktype = models.ForeignKey(BlockType, default=1,
                                  on_delete=models.PROTECT, related_name='+')
    name = models.CharField(max_length=100)
    sort_order = models.IntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['blocktype', 'name'],
                                    name='unique_blocktype_name')
        ]


class ParameterDataType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class CommonBlock(models.Model):
    p000_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p001_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p002_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p003_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p004_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p005_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p006_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p007_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p008_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p009_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p010_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p011_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p012_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p013_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p014_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p015_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p016_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p017_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p018_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p019_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p020_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p021_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p022_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p023_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p024_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p025_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p026_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p027_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p028_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p029_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p030_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p031_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p032_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p033_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p034_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p035_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p036_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p037_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p038_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p039_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p040_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p041_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p042_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p043_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p044_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p045_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p046_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p047_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p048_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p049_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p050_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p051_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p052_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p053_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p054_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p055_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p056_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p057_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p058_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p059_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)

    class Meta:
        abstract = True


class CommonBlockParameter(models.Model):
    p000 = models.CharField(max_length=100, blank=True, null=True)
    p000_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p000_help = models.CharField(max_length=100, blank=True, null=True)
    p001 = models.CharField(max_length=100, blank=True, null=True)
    p001_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p001_help = models.CharField(max_length=100, blank=True, null=True)
    p002 = models.CharField(max_length=100, blank=True, null=True)
    p002_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p002_help = models.CharField(max_length=100, blank=True, null=True)
    p003 = models.CharField(max_length=100, blank=True, null=True)
    p003_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p003_help = models.CharField(max_length=100, blank=True, null=True)
    p004 = models.CharField(max_length=100, blank=True, null=True)
    p004_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p004_help = models.CharField(max_length=100, blank=True, null=True)
    p005 = models.CharField(max_length=100, blank=True, null=True)
    p005_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p005_help = models.CharField(max_length=100, blank=True, null=True)
    p006 = models.CharField(max_length=100, blank=True, null=True)
    p006_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p006_help = models.CharField(max_length=100, blank=True, null=True)
    p007 = models.CharField(max_length=100, blank=True, null=True)
    p007_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p007_help = models.CharField(max_length=100, blank=True, null=True)
    p008 = models.CharField(max_length=100, blank=True, null=True)
    p008_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p008_help = models.CharField(max_length=100, blank=True, null=True)
    p009 = models.CharField(max_length=100, blank=True, null=True)
    p009_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p009_help = models.CharField(max_length=100, blank=True, null=True)
    p010 = models.CharField(max_length=100, blank=True, null=True)
    p010_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p010_help = models.CharField(max_length=100, blank=True, null=True)
    p011 = models.CharField(max_length=100, blank=True, null=True)
    p011_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p011_help = models.CharField(max_length=100, blank=True, null=True)
    p012 = models.CharField(max_length=100, blank=True, null=True)
    p012_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p012_help = models.CharField(max_length=100, blank=True, null=True)
    p013 = models.CharField(max_length=100, blank=True, null=True)
    p013_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p013_help = models.CharField(max_length=100, blank=True, null=True)
    p014 = models.CharField(max_length=100, blank=True, null=True)
    p014_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p014_help = models.CharField(max_length=100, blank=True, null=True)
    p015 = models.CharField(max_length=100, blank=True, null=True)
    p015_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p015_help = models.CharField(max_length=100, blank=True, null=True)
    p016 = models.CharField(max_length=100, blank=True, null=True)
    p016_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p016_help = models.CharField(max_length=100, blank=True, null=True)
    p017 = models.CharField(max_length=100, blank=True, null=True)
    p017_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p017_help = models.CharField(max_length=100, blank=True, null=True)
    p018 = models.CharField(max_length=100, blank=True, null=True)
    p018_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p018_help = models.CharField(max_length=100, blank=True, null=True)
    p019 = models.CharField(max_length=100, blank=True, null=True)
    p019_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p019_help = models.CharField(max_length=100, blank=True, null=True)
    p020 = models.CharField(max_length=100, blank=True, null=True)
    p020_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p020_help = models.CharField(max_length=100, blank=True, null=True)
    p021 = models.CharField(max_length=100, blank=True, null=True)
    p021_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p021_help = models.CharField(max_length=100, blank=True, null=True)
    p022 = models.CharField(max_length=100, blank=True, null=True)
    p022_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p022_help = models.CharField(max_length=100, blank=True, null=True)
    p023 = models.CharField(max_length=100, blank=True, null=True)
    p023_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p023_help = models.CharField(max_length=100, blank=True, null=True)
    p024 = models.CharField(max_length=100, blank=True, null=True)
    p024_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p024_help = models.CharField(max_length=100, blank=True, null=True)
    p025 = models.CharField(max_length=100, blank=True, null=True)
    p025_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p025_help = models.CharField(max_length=100, blank=True, null=True)
    p026 = models.CharField(max_length=100, blank=True, null=True)
    p026_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p026_help = models.CharField(max_length=100, blank=True, null=True)
    p027 = models.CharField(max_length=100, blank=True, null=True)
    p027_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p027_help = models.CharField(max_length=100, blank=True, null=True)
    p028 = models.CharField(max_length=100, blank=True, null=True)
    p028_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p028_help = models.CharField(max_length=100, blank=True, null=True)
    p029 = models.CharField(max_length=100, blank=True, null=True)
    p029_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p029_help = models.CharField(max_length=100, blank=True, null=True)
    p030 = models.CharField(max_length=100, blank=True, null=True)
    p030_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p030_help = models.CharField(max_length=100, blank=True, null=True)
    p031 = models.CharField(max_length=100, blank=True, null=True)
    p031_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p031_help = models.CharField(max_length=100, blank=True, null=True)
    p032 = models.CharField(max_length=100, blank=True, null=True)
    p032_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p032_help = models.CharField(max_length=100, blank=True, null=True)
    p033 = models.CharField(max_length=100, blank=True, null=True)
    p033_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p033_help = models.CharField(max_length=100, blank=True, null=True)
    p034 = models.CharField(max_length=100, blank=True, null=True)
    p034_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p034_help = models.CharField(max_length=100, blank=True, null=True)
    p035 = models.CharField(max_length=100, blank=True, null=True)
    p035_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p035_help = models.CharField(max_length=100, blank=True, null=True)
    p036 = models.CharField(max_length=100, blank=True, null=True)
    p036_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p036_help = models.CharField(max_length=100, blank=True, null=True)
    p037 = models.CharField(max_length=100, blank=True, null=True)
    p037_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p037_help = models.CharField(max_length=100, blank=True, null=True)
    p038 = models.CharField(max_length=100, blank=True, null=True)
    p038_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p038_help = models.CharField(max_length=100, blank=True, null=True)
    p039 = models.CharField(max_length=100, blank=True, null=True)
    p039_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p039_help = models.CharField(max_length=100, blank=True, null=True)
    p040 = models.CharField(max_length=100, blank=True, null=True)
    p040_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p040_help = models.CharField(max_length=100, blank=True, null=True)
    p041 = models.CharField(max_length=100, blank=True, null=True)
    p041_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p041_help = models.CharField(max_length=100, blank=True, null=True)
    p042 = models.CharField(max_length=100, blank=True, null=True)
    p042_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p042_help = models.CharField(max_length=100, blank=True, null=True)
    p043 = models.CharField(max_length=100, blank=True, null=True)
    p043_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p043_help = models.CharField(max_length=100, blank=True, null=True)
    p044 = models.CharField(max_length=100, blank=True, null=True)
    p044_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p044_help = models.CharField(max_length=100, blank=True, null=True)
    p045 = models.CharField(max_length=100, blank=True, null=True)
    p045_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p045_help = models.CharField(max_length=100, blank=True, null=True)
    p046 = models.CharField(max_length=100, blank=True, null=True)
    p046_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p046_help = models.CharField(max_length=100, blank=True, null=True)
    p047 = models.CharField(max_length=100, blank=True, null=True)
    p047_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p047_help = models.CharField(max_length=100, blank=True, null=True)
    p048 = models.CharField(max_length=100, blank=True, null=True)
    p048_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p048_help = models.CharField(max_length=100, blank=True, null=True)
    p049 = models.CharField(max_length=100, blank=True, null=True)
    p049_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p049_help = models.CharField(max_length=100, blank=True, null=True)
    p050 = models.CharField(max_length=100, blank=True, null=True)
    p050_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p050_help = models.CharField(max_length=100, blank=True, null=True)
    p051 = models.CharField(max_length=100, blank=True, null=True)
    p051_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p051_help = models.CharField(max_length=100, blank=True, null=True)
    p052 = models.CharField(max_length=100, blank=True, null=True)
    p052_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p052_help = models.CharField(max_length=100, blank=True, null=True)
    p053 = models.CharField(max_length=100, blank=True, null=True)
    p053_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p053_help = models.CharField(max_length=100, blank=True, null=True)
    p054 = models.CharField(max_length=100, blank=True, null=True)
    p054_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p054_help = models.CharField(max_length=100, blank=True, null=True)
    p055 = models.CharField(max_length=100, blank=True, null=True)
    p055_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p055_help = models.CharField(max_length=100, blank=True, null=True)
    p056 = models.CharField(max_length=100, blank=True, null=True)
    p056_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p056_help = models.CharField(max_length=100, blank=True, null=True)
    p057 = models.CharField(max_length=100, blank=True, null=True)
    p057_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p057_help = models.CharField(max_length=100, blank=True, null=True)
    p058 = models.CharField(max_length=100, blank=True, null=True)
    p058_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p058_help = models.CharField(max_length=100, blank=True, null=True)
    p059 = models.CharField(max_length=100, blank=True, null=True)
    p059_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p059_help = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True


class BlockPrefix(CommonBlock):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class BlockPrefixParameter(CommonBlockParameter):
    id = models.AutoField(primary_key=True)
    blockprefix = models.ForeignKey(BlockPrefix, on_delete=models.PROTECT)

    def __str__(self):
        """String for representing the Model object."""
        return self.blockprefix.name


class Block(CommonBlock):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    blockprefix = models.ForeignKey(BlockPrefix, default=1,
                                    on_delete=models.PROTECT, related_name='+')
    main_category = models.ForeignKey(Category, null=True,
                                      on_delete=models.PROTECT, related_name='+')
    categories = models.ManyToManyField(Category)
    block_name = models.CharField(max_length=200,
                                  unique=True, null=True)
    initial_display_parameter = models.CharField(max_length=100,
                                                 blank=True, null=True)
    simulation_function = models.CharField(max_length=100,
                                           blank=True, null=True)
    block_image_path = models.CharField(max_length=100,
                                        blank=True, null=True)
    block_width = models.IntegerField(default=40)
    block_height = models.IntegerField(default=40)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['main_category', 'name'],
                                    name='unique_category_name')
        ]


class BlockParameter(CommonBlockParameter):
    id = models.AutoField(primary_key=True)
    block = models.OneToOneField(Block, on_delete=models.PROTECT)

    def __str__(self):
        """String for representing the Model object."""
        return self.block.name


class NewBlock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    blockprefix = models.ForeignKey(BlockPrefix, default=1,
                                    on_delete=models.PROTECT, related_name='+')
    main_category = models.ForeignKey(Category, null=True,
                                      on_delete=models.PROTECT, related_name='+')
    categories = models.ManyToManyField(Category)
    block_name = models.CharField(max_length=200,
                                  unique=True, null=True)
    initial_display_parameter = models.CharField(max_length=100,
                                                 blank=True, null=True)
    simulation_function = models.CharField(max_length=100,
                                           blank=True, null=True)
    block_image_path = models.CharField(max_length=100,
                                        blank=True, null=True)
    block_width = models.IntegerField(default=40)
    block_height = models.IntegerField(default=40)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['main_category', 'name'],
                                    name='unique_main_category_name')
        ]


class NewBlockParameter(models.Model):
    id = models.AutoField(primary_key=True)
    block = models.ForeignKey(NewBlock, on_delete=models.PROTECT)
    p_order = models.IntegerField()
    p_label = models.CharField(max_length=100, blank=False)
    p_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                               related_name='+')
    p_help = models.CharField(max_length=100, blank=True, null=True)
    p_value_initial = models.CharField(max_length=100, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.block.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['block', 'p_order'],
                                    name='unique_block_p_order')
        ]


class NewBlockPort(models.Model):
    id = models.AutoField(primary_key=True)
    block = models.ForeignKey(NewBlock, on_delete=models.PROTECT)
    port_order = models.IntegerField()
    port_name = models.CharField(max_length=100)
    port_number = models.CharField(max_length=10)
    port_x = models.IntegerField(default=1)
    port_y = models.IntegerField(default=1)
    port_orientation = models.CharField(max_length=100)
    port_part = models.IntegerField(default=1)
    port_dmg = models.IntegerField(default=1)
    port_type = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return '%s %s' % (self.block.name, self.port_order)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['block', 'port_order'],
                                    name='unique_blocktemp_port_order')
        ]
