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


class BlockPrefix(CommonBlock):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


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
