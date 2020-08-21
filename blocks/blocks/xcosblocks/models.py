from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    sort_order = models.IntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class ParameterDataType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Block(models.Model):
    name = models.CharField(max_length=100, unique=True)
    categories = models.ManyToManyField(Category)
    initial_explicit_input_ports = models.IntegerField()
    initial_implicit_input_ports = models.IntegerField()
    initial_explicit_output_ports = models.IntegerField()
    initial_implicit_output_ports = models.IntegerField()
    initial_control_ports = models.IntegerField()
    initial_command_ports = models.IntegerField()
    initial_display_parameter = models.CharField(max_length=100)
    variable_explicit_input_ports = models.CharField(max_length=100)
    variable_implicit_input_ports = models.CharField(max_length=100)
    variable_explicit_output_ports = models.CharField(max_length=100)
    variable_implicit_output_ports = models.CharField(max_length=100)
    variable_control_ports = models.CharField(max_length=100)
    variable_command_ports = models.CharField(max_length=100)
    variable_display_parameter = models.CharField(max_length=100)
    p000 = models.CharField(max_length=100, blank=True, null=True)
    p000_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p000_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p001 = models.CharField(max_length=100, blank=True, null=True)
    p001_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p001_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p002 = models.CharField(max_length=100, blank=True, null=True)
    p002_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p002_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p003 = models.CharField(max_length=100, blank=True, null=True)
    p003_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p003_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p004 = models.CharField(max_length=100, blank=True, null=True)
    p004_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p004_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p005 = models.CharField(max_length=100, blank=True, null=True)
    p005_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p005_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p006 = models.CharField(max_length=100, blank=True, null=True)
    p006_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p006_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p007 = models.CharField(max_length=100, blank=True, null=True)
    p007_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p007_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p008 = models.CharField(max_length=100, blank=True, null=True)
    p008_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p008_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p009 = models.CharField(max_length=100, blank=True, null=True)
    p009_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p009_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p010 = models.CharField(max_length=100, blank=True, null=True)
    p010_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p010_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p011 = models.CharField(max_length=100, blank=True, null=True)
    p011_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p011_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p012 = models.CharField(max_length=100, blank=True, null=True)
    p012_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p012_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p013 = models.CharField(max_length=100, blank=True, null=True)
    p013_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p013_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p014 = models.CharField(max_length=100, blank=True, null=True)
    p014_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p014_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p015 = models.CharField(max_length=100, blank=True, null=True)
    p015_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p015_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p016 = models.CharField(max_length=100, blank=True, null=True)
    p016_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p016_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p017 = models.CharField(max_length=100, blank=True, null=True)
    p017_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p017_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p018 = models.CharField(max_length=100, blank=True, null=True)
    p018_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p018_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p019 = models.CharField(max_length=100, blank=True, null=True)
    p019_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p019_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p020 = models.CharField(max_length=100, blank=True, null=True)
    p020_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p020_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p021 = models.CharField(max_length=100, blank=True, null=True)
    p021_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p021_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p022 = models.CharField(max_length=100, blank=True, null=True)
    p022_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p022_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p023 = models.CharField(max_length=100, blank=True, null=True)
    p023_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p023_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p024 = models.CharField(max_length=100, blank=True, null=True)
    p024_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p024_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p025 = models.CharField(max_length=100, blank=True, null=True)
    p025_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p025_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p026 = models.CharField(max_length=100, blank=True, null=True)
    p026_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p026_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p027 = models.CharField(max_length=100, blank=True, null=True)
    p027_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p027_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p028 = models.CharField(max_length=100, blank=True, null=True)
    p028_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p028_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p029 = models.CharField(max_length=100, blank=True, null=True)
    p029_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p029_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p030 = models.CharField(max_length=100, blank=True, null=True)
    p030_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p030_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p031 = models.CharField(max_length=100, blank=True, null=True)
    p031_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p031_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p032 = models.CharField(max_length=100, blank=True, null=True)
    p032_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p032_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p033 = models.CharField(max_length=100, blank=True, null=True)
    p033_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p033_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p034 = models.CharField(max_length=100, blank=True, null=True)
    p034_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p034_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p035 = models.CharField(max_length=100, blank=True, null=True)
    p035_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p035_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p036 = models.CharField(max_length=100, blank=True, null=True)
    p036_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p036_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p037 = models.CharField(max_length=100, blank=True, null=True)
    p037_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p037_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p038 = models.CharField(max_length=100, blank=True, null=True)
    p038_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p038_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)
    p039 = models.CharField(max_length=100, blank=True, null=True)
    p039_type = models.ForeignKey(ParameterDataType, on_delete=models.PROTECT,
                                  related_name='+', blank=True, null=True)
    p039_value_initial = models.CharField(max_length=100,
                                          blank=True, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
