from django.http import JsonResponse
from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
import io
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category, Block, BlockParameter, BlockPort
from .serializers import CategorySerializer, BlockSerializer, \
    BlockParameterSerializer, BlockPortSerializer, ErrorSerializer, \
    SetBlockParameterSerializer


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
            'id': ['exact'],
            'name': ['istartswith'],
            'categories': ['exact'],
        }


class BlockViewSet(ReadOnlyModelViewSet):
    """
     Listing All Block Details
    """
    queryset = Block.objects.all().order_by('name')
    queryset = BlockSerializer.prefetch_category(queryset)
    queryset = BlockSerializer.prefetch_blockport(queryset)
    serializer_class = BlockSerializer
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_class = BlockFilterSet


class BlockParameterFilterSet(FilterSet):
    class Meta:
        model = BlockParameter
        fields = {
            'block': ['exact'],
        }


class BlockParameterViewSet(ReadOnlyModelViewSet):
    """
     Listing All Block Parameter Details
    """
    queryset = BlockParameter.objects.all()
    serializer_class = BlockParameterSerializer
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_class = BlockParameterFilterSet


class BlockPortFilterSet(FilterSet):
    class Meta:
        model = BlockPort
        fields = {
            'block': ['exact'],
        }


class BlockPortViewSet(ReadOnlyModelViewSet):
    """
     Listing All Block Port Details
    """
    queryset = BlockPort.objects.all()
    serializer_class = BlockPortSerializer
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_class = BlockPortFilterSet


def set_block_parameter(request):
    if request.method == 'POST':
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        serializer = SetBlockParameterSerializer(data=data)
        if serializer.is_valid():
            # process the data to get port
            try:
                port = serializer.getblockportserializer()
                return JsonResponse(port.initial_data)
            except Exception as e:
                error = 'getblockportserializer error: %s' % str(e)
                errorserializer = ErrorSerializer(data={
                    'code': 500, 'error': error})
                return JsonResponse(errorserializer.initial_data)
        else:
            error = 'getblockportserializer errors: %s' % serializer.errors
            errorserializer = ErrorSerializer(data={
                'code': 500, 'error': error})
            return JsonResponse(errorserializer.initial_data)
    else:
        serializer = SetBlockParameterSerializer()

    return JsonResponse(serializer.data)
