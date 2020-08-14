from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet

from . import models, serializers


class CategoryFilterSet(FilterSet):
    class Meta:
        model = models.Category
        fields = {
            'name': ['icontains'],
        }


class CategoryViewSet(ReadOnlyModelViewSet):
    """
     Listing All Category Details
    """
    queryset = models.Category.objects.all().order_by('sort_order')
    serializer_class = serializers.CategorySerializer
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_class = CategoryFilterSet


class BlockFilterSet(FilterSet):
    class Meta:
        model = models.Block
        fields = {
            'name': ['icontains'],
        }


class BlockViewSet(ReadOnlyModelViewSet):
    """
     Listing All Block Details
    """
    queryset = models.Block.objects.all()
    serializer_class = serializers.BlockSerializer
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_class = BlockFilterSet
