from django.contrib.auth import get_user_model
import django_filters
from django_filters import rest_framework as filters
import logging
from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
import traceback
import uuid
from .models import Gallery, StateSave, BookCategory, Book
from .serializers import Base64ImageField, GalleryListSerializer, GalleryDetailSerializer, \
    SaveListSerializer, StateSaveSerializer, BookCategorySerializer, \
    BookSerializer

from django.db.models import Count, OuterRef, Subquery

logger = logging.getLogger(__name__)


class StateSaveView(APIView):
    '''
    API to save the state of project to db which can be loaded or shared later
    Note: this is different from SnapshotSave which stores images
    THIS WILL ESCAPE DOUBLE QUOTES
    '''

    # Permissions should be validated here
    permission_classes = (AllowAny,)
    # parser_classes = (FormParser,)

    def post(self, request):
        logger.info('Got POST for state save=%s', request.data.get('name'))
        try:
            state_save = StateSave(
                data_dump=request.data.get('data_dump'),
                script_dump=request.data.get('script_dump'),
                description=request.data.get('description'),
                name=request.data.get('name'),
                owner=request.user if request.user.is_authenticated else None,
                shared=True,
            )
            state_save.save()

            img = Base64ImageField(max_length=None, use_url=True)
            filename, content = img.update(request.data['base64_image'])
            state_save.base64_image.save(filename, content)

            logger.info('Saved state=%s', str(state_save))
            return Response(SaveListSerializer(state_save).data)
        except Exception as e:
            logger.error('Error saving state=%s', e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CopyStateView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, JSONParser)

    def post(self, request, save_id):
        if isinstance(save_id, uuid.UUID):
            # Check for permissions and sharing settings here
            try:
                state_save = StateSave.objects.get(
                    save_id=save_id)
            except StateSave.DoesNotExist:
                return Response({'error': 'Does not Exist'},
                                status=status.HTTP_404_NOT_FOUND)
            copy_state = StateSave(name=state_save.name,
                                   description=state_save.description,
                                   data_dump=state_save.data_dump,
                                   base64_image=state_save.base64_image,
                                   owner=self.request.user)
            copy_state.save()
            return Response(
                {"save_id": copy_state.save_id})


class FetchSaveDiagram(APIView):
    """
    Returns Saved data for given save id ,
    Only user who saved the state can access / update it
    THIS WILL ESCAPE DOUBLE QUOTES

    """
    permission_classes = (AllowAny,)
    parser_classes = (FormParser, JSONParser)
    methods = ['GET']

    def get(self, request, save_id):
        logger.info('Got GET for state save id=%s', save_id)

        if not isinstance(save_id, uuid.UUID):
            return Response({'error': 'Invalid sharing state'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check for permissions and sharing settings here
        try:
            state_save = StateSave.objects.get(save_id=save_id)
        except StateSave.DoesNotExist:
            return Response({'error': 'Does not Exist'},
                            status=status.HTTP_404_NOT_FOUND)

        # Verifies owner
        if self.request.user != state_save.owner and not state_save.shared:
            return Response({'error': 'not the owner and not shared'},
                            status=status.HTTP_401_UNAUTHORIZED)

        try:
            serialized = StateSaveSerializer(state_save, context={'request': request})
            data = {}
            data.update(serialized.data)

            User = get_user_model()
            try:
                owner_name = User.objects.get(id=serialized.data.get('owner'))
                data['owner'] = owner_name.username
            except User.DoesNotExist:
                data['owner'] = None

            return Response(data)
        except Exception:
            traceback.print_exc()
            return Response({'error': 'Not Able To Serialize'},
                            status=status.HTTP_400_BAD_REQUEST)

    def update_state(self, state, data):
        # if data dump, shared, name, or description needs to be updated
        if 'data_dump' in data:
            state.data_dump = data['data_dump']
        if 'script_dump' in data:
            state.script_dump = data['script_dump']
        if 'shared' in data:
            state.shared = bool(data['shared'])
        if 'name' in data:
            state.name = data['name']
        if 'description' in data:
            state.description = data['description']
        # if thumbnail needs to be updated
        if 'base64_image' in data:
            img = Base64ImageField(max_length=None, use_url=True)
            filename, content = img.update(data['base64_image'])
            state.base64_image.save(filename, content)

    def post(self, request, save_id):
        logger.info('Got POST for state save id=%s', save_id)

        if not isinstance(save_id, uuid.UUID):
            return Response({'error': 'Invalid sharing state'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check for permissions and sharing settings here
        try:
            state_save = StateSave.objects.get(save_id=save_id)
        except StateSave.DoesNotExist:
            return Response({'error': 'Does not Exist'},
                            status=status.HTTP_404_NOT_FOUND)

        # Verifies owner
        if self.request.user != state_save.owner:
            return Response({'error': 'not the owner'},
                            status=status.HTTP_401_UNAUTHORIZED)

        if not request.data['data_dump'] and not request.data['shared']:
            return Response({'error': 'not a valid POST request'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

        try:
            self.update_state(state_save, request.data)
            state_save.save()
            logger.info('Saved state=%s', str(state_save))
            return Response(SaveListSerializer(state_save).data)
        except Exception as e:
            logger.error('Error saving state=%s', e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, save_id):
        if isinstance(save_id, uuid.UUID):
            try:
                state_save = StateSave.objects.get(
                    save_id=save_id,
                    owner=self.request.user)
            except StateSave.DoesNotExist:
                return Response({'error': 'Does not Exist'},
                                status=status.HTTP_404_NOT_FOUND)
            state_save.delete()
            return Response({'done': True})
        else:
            return Response({'error': 'Invalid sharing state'},
                            status=status.HTTP_400_BAD_REQUEST)


class StateShareView(APIView):
    """
    Enables sharing for the given saved state
    Note: Only authorized user can do this

    """
    permission_classes = (AllowAny,)
    methods = ['GET']

    def post(self, request, save_id, sharing):

        if isinstance(save_id, uuid.UUID):
            # Check for permissions and sharing settings here
            try:
                state_save = StateSave.objects.get(
                    save_id=save_id)
            except StateSave.DoesNotExist:
                return Response({'error': 'Does not Exist'},
                                status=status.HTTP_404_NOT_FOUND)

            # Verifies owner
            if self.request.user != state_save.owner:
                return Response({'error': 'Not the owner'},
                                status=status.HTTP_401_UNAUTHORIZED)
            try:
                if sharing == 'on':
                    state_save.shared = True
                elif sharing == 'off':
                    state_save.shared = False
                else:
                    return Response({'error': 'Invalid sharing state'},
                                    status=status.HTTP_400_BAD_REQUEST)
                state_save.save()
                serialized = StateSaveSerializer(state_save)
                return Response(serialized.data)
            except Exception:
                return Response(serialized.error)
        else:
            return Response({'error': 'Invalid sharing state'},
                            status=status.HTTP_400_BAD_REQUEST)


class UserSavesView(APIView):
    """
    Returns Saved data for given username,
    Only user who saved the state can access it
    THIS WILL ESCAPE DOUBLE QUOTES

    """
    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, JSONParser)
    methods = ['GET']

    def get(self, request):
        try:
            state_save = StateSave.objects.filter(
                owner=self.request.user
            ).order_by('-save_time')

            # Serialize the data
            serialized = StateSaveSerializer(state_save, many=True)
            return Response(serialized.data)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SaveSearchFilterSet(django_filters.FilterSet):
    class Meta:
        model = StateSave
        fields = {
            'name': ['icontains'],
            'description': ['icontains'],
            'save_time': ['icontains'],
            'create_time': ['icontains'],
        }


class SaveSearchViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Search Project
    """

    def get_queryset(self):
        queryset = StateSave.objects.filter(
            owner=self.request.user).order_by('-save_time')
        return queryset

    serializer_class = SaveListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SaveSearchFilterSet


class DeleteDiagram(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, save_id):
        try:
            queryset = StateSave.objects.filter(
                save_id=save_id,
                owner=self.request.user
            )
            if queryset[0].project is None:
                queryset.delete()
                return Response(data=None, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
        except StateSave.DoesNotExist:
            return Response({"error": "Diagram not found"},
                            status=status.HTTP_404_NOT_FOUND)


class GalleryListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = GalleryListSerializer

    def get_queryset(self):
        queryset = Gallery.objects.all()
        book_id = self.request.query_params.get('book_id')
        if book_id:
            queryset = queryset.filter(book_id=book_id)
        return queryset


class GalleryDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Gallery.objects.all()
    serializer_class = GalleryDetailSerializer
    lookup_field = 'save_id'


class BookCategoryView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


class BookView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Book.objects.annotate(example_count=Count('examples')).order_by('book_name', 'author_name')
    serializer_class = BookSerializer
