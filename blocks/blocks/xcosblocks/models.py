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


class BlockPrefix(models.Model):
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
