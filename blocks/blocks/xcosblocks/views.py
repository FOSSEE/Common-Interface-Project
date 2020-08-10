import django_filters
from rest_framework import viewsets
from . import models
from . import serializers


class CategoryFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.Category
        fields = {
            'name': ['icontains'],
        }


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
     Listing All Category Details
    """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend
    ]
    filterset_class = CategoryFilterSet


class BlockFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.Block
        fields = {
            'name': ['icontains'],
        }


class BlockViewSet(viewsets.ReadOnlyModelViewSet):
    """
     Listing All Block Details
    """
    queryset = models.Block.objects.all()
    serializer_class = serializers.BlockSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend
    ]
    filterset_class = BlockFilterSet
