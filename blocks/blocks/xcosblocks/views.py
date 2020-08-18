from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category, Block
from .serializers import CategorySerializer, BlockSerializer


class CategoryFilterSet(FilterSet):
    class Meta:
        model = Category
        fields = {
            'name': ['icontains'],
        }


class CategoryViewSet(ReadOnlyModelViewSet):
    """
     Listing All Category Details
    """
    queryset = Category.objects.all().order_by('sort_order')
    serializer_class = CategorySerializer
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_class = CategoryFilterSet


class BlockFilterSet(FilterSet):
    class Meta:
        model = Block
        fields = {
            'name': ['istartswith'],
            'categories': ['exact'],
        }


class BlockViewSet(ReadOnlyModelViewSet):
    """
     Listing All Block Details
    """
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_class = BlockFilterSet
