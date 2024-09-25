from django.http import JsonResponse
from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
import io
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category, \
    NewBlock, NewBlockParameter, NewBlockPort
from .serializers import CategorySerializer, \
    ErrorSerializer, \
    SetBlockParameterSerializer, \
    NewBlockSerializer, NewBlockParameterSerializer, NewBlockPortSerializer


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


def get_block_images(request):
    if request.method == 'GET':
        queryset = NewBlock.objects.all().values_list('block_image_path', flat=True)
        return JsonResponse(list(queryset), safe=False)


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
                return JsonResponse(errorserializer.initial_data, safe=False)
        else:
            error = 'getblockportserializer errors: %s' % serializer.errors
            errorserializer = ErrorSerializer(data={
                'code': 500, 'error': error})
            return JsonResponse(errorserializer.initial_data, safe=False)
    else:
        serializer = SetBlockParameterSerializer()

    return JsonResponse(serializer.initial_data)


class NewBlockFilterSet(FilterSet):
    class Meta:
        model = NewBlock
        fields = {
            'id': ['exact'],
            'name': ['istartswith'],
            'categories': ['exact'],
        }


class NewBlockViewSet(ReadOnlyModelViewSet):
    """
     Listing All Block Details
    """
    queryset = NewBlock.objects.all().order_by('name')
    queryset = NewBlockSerializer.prefetch_category(queryset)
    queryset = NewBlockSerializer.prefetch_blockparameter(queryset)
    queryset = NewBlockSerializer.prefetch_blockport(queryset)
    serializer_class = NewBlockSerializer
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_class = NewBlockFilterSet


class NewBlockParameterFilterSet(FilterSet):
    class Meta:
        model = NewBlockParameter
        fields = {
            'block': ['exact'],
            'block__name': ['exact'],
        }


class NewBlockParameterViewSet(ReadOnlyModelViewSet):
    """
     Listing All Block Parameter Details
    """
    queryset = NewBlockParameter.objects.all().order_by('block_id', 'p_order')
    serializer_class = NewBlockParameterSerializer
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_class = NewBlockParameterFilterSet


class NewBlockPortFilterSet(FilterSet):
    class Meta:
        model = NewBlockPort
        fields = {
            'block': ['exact'],
        }


class NewBlockPortViewSet(ReadOnlyModelViewSet):
    """
     Listing All Block Port Details
    """
    queryset = NewBlockPort.objects.all()
    serializer_class = NewBlockPortSerializer
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_class = NewBlockPortFilterSet
