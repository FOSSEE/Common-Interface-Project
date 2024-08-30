from django.contrib.auth import get_user_model
import django_filters
from django_filters import rest_framework as filters
from drf_yasg.utils import swagger_auto_schema
import logging
from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import traceback
import uuid
from .models import Gallery, StateSave
from .serializers import Base64ImageField, GallerySerializer, \
    SaveListSerializer, StateSaveSerializer
from django.db.models import OuterRef, Subquery

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

    @swagger_auto_schema(request_body=StateSaveSerializer)
    def post(self, request, *args, **kwargs):
        print("Getting Saved State")

        logger.info('Got POST for state save ')
        try:
            queryset = StateSave.objects.get(
                save_id=request.data.get("save_id", None))
            serializer = StateSaveSerializer(data=request.data)
            if serializer.is_valid():
                img = Base64ImageField(max_length=None, use_url=True)
                filename, content = img.update(request.data['base64_image'])
                queryset.data_dump = request.data.get("data_dump")
                queryset.save()
                queryset.base64_image.save(filename, content)
                return Response(data=serializer.data,
                                status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        except StateSave.DoesNotExist:
            try:
                queryset = StateSave.objects.get(
                    save_id=request.data.get("save_id", None),
                    data_dump=request.data["data_dump"])
                serializer = StateSaveSerializer(data=request.data)
                if serializer.is_valid():
                    queryset.name = serializer.data["name"]
                    queryset.description = serializer.data["description"]
                    queryset.save()
                    response = serializer.data
                    response['duplicate'] = True
                    response['owner'] = queryset.owner.username
                    return Response(response)
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
            except StateSave.DoesNotExist:
                img = Base64ImageField(max_length=None, use_url=True)
                filename, content = img.update(request.data['base64_image'])
                try:
                    state_save = StateSave(
                        data_dump=request.data.get('data_dump'),
                        description=request.data.get('description'),
                        name=request.data.get('name'),
                        owner=request.user if request.user.is_authenticated else None,
                        shared=True,
                    )
                except Exception:
                    state_save = StateSave(
                        data_dump=request.data.get('data_dump'),
                        description=request.data.get('description'),
                        name=request.data.get('name'),
                        owner=request.user if request.user.is_authenticated else None,
                    )
                if request.data.get('save_id'):
                    state_save.save_id = request.data.get('save_id')
                state_save.base64_image.save(filename, content)
                try:
                    state_save.save()
                    return Response(StateSaveSerializer(state_save).data)
                except Exception:
                    return Response(status=status.HTTP_400_BAD_REQUEST)


class CopyStateView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, JSONParser)

    def post(self, request, save_id):
        if isinstance(save_id, uuid.UUID):
            # Check for permissions and sharing settings here
            try:
                saved_state = StateSave.objects.get(
                    save_id=save_id)
            except StateSave.DoesNotExist:
                return Response({'error': 'Does not Exist'},
                                status=status.HTTP_404_NOT_FOUND)
            copy_state = StateSave(name=saved_state.name,
                                   description=saved_state.description,
                                   data_dump=saved_state.data_dump,
                                   base64_image=saved_state.base64_image,
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

    @swagger_auto_schema(responses={200: StateSaveSerializer})
    def get(self, request, save_id):

        if isinstance(save_id, uuid.UUID):
            # Check for permissions and sharing settings here
            try:
                saved_state = StateSave.objects.get(
                    save_id=save_id)
            except StateSave.DoesNotExist:
                return Response({'error': 'Does not Exist'},
                                status=status.HTTP_404_NOT_FOUND)
            # Verifies owner
            if self.request.user != saved_state.owner and not saved_state.shared:
                print("Here")
                return Response({'error': 'not the owner and not shared'},
                                status=status.HTTP_401_UNAUTHORIZED)
            try:
                serialized = StateSaveSerializer(
                    saved_state, context={'request': request})
                User = get_user_model()
                try:
                    owner_name = User.objects.get(
                        id=serialized.data.get('owner'))
                    data = {}
                    data.update(serialized.data)
                    data['owner'] = owner_name.username
                except User.DoesNotExist:
                    data = {}
                    data.update(serialized.data)
                    data['owner'] = None
                return Response(data)
            except Exception:
                traceback.print_exc()
                return Response({'error': 'Not Able To Serialize'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid sharing state'},
                            status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: StateSaveSerializer})
    def post(self, request, save_id):
        if isinstance(save_id, uuid.UUID):
            # Check for permissions and sharing settings here
            try:
                saved_state = StateSave.objects.get(save_id=save_id)
            except StateSave.DoesNotExist:
                return Response({'error': 'Does not Exist'},
                                status=status.HTTP_404_NOT_FOUND)

            # Verifies owner
            if self.request.user != saved_state.owner:
                return Response({'error': 'not the owner and not shared'},
                                status=status.HTTP_401_UNAUTHORIZED)

            if not request.data['data_dump'] and not request.data['shared']:
                return Response({'error': 'not a valid PUT request'},
                                status=status.HTTP_406_NOT_ACCEPTABLE)

            try:
                # if data dump, shared,name and description needs to be updated
                if 'data_dump' in request.data:
                    saved_state.data_dump = request.data['data_dump']
                if 'shared' in request.data:
                    saved_state.shared = bool(request.data['shared'])
                if 'name' in request.data:
                    saved_state.name = request.data['name']
                if 'description' in request.data:
                    saved_state.description = request.data['description']
                # if thumbnail needs to be updated
                if 'base64_image' in request.data:
                    img = Base64ImageField(max_length=None, use_url=True)
                    filename, content = img.update(
                        request.data['base64_image'])
                    saved_state.base64_image.save(filename, content)
                saved_state.save()
                serialized = SaveListSerializer(saved_state)
                return Response(serialized.data)
            except Exception:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'Invalid sharing state'},
                            status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: StateSaveSerializer})
    def delete(self, request, save_id):
        if isinstance(save_id, uuid.UUID):
            try:
                saved_state = StateSave.objects.get(
                    save_id=save_id,
                    owner=self.request.user)
            except StateSave.DoesNotExist:
                return Response({'error': 'Does not Exist'},
                                status=status.HTTP_404_NOT_FOUND)
            saved_state.delete()
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

    @swagger_auto_schema(responses={200: StateSaveSerializer})
    def post(self, request, save_id, sharing):

        if isinstance(save_id, uuid.UUID):
            # Check for permissions and sharing settings here
            try:
                saved_state = StateSave.objects.get(
                    save_id=save_id)
            except StateSave.DoesNotExist:
                return Response({'error': 'Does not Exist'},
                                status=status.HTTP_404_NOT_FOUND)

            # Verifies owner
            if self.request.user != saved_state.owner:
                return Response({'error': 'Not the owner'},
                                status=status.HTTP_401_UNAUTHORIZED)
            try:
                if sharing == 'on':
                    saved_state.shared = True
                elif sharing == 'off':
                    saved_state.shared = False
                else:
                    return Response({'error': 'Invalid sharing state'},
                                    status=status.HTTP_400_BAD_REQUEST)
                saved_state.save()
                serialized = StateSaveSerializer(saved_state)
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

    @swagger_auto_schema(responses={200: StateSaveSerializer})
    def get(self, request):
        try:
            # Subquery to get the latest save_time for each save_id
            latest_save_time_subquery = StateSave.objects.filter(
                save_id=OuterRef('save_id'),
                owner=self.request.user
            ).order_by('-save_time').values('save_time')[:1]

            # Annotate the main query with the latest save time
            saved_state = StateSave.objects.filter(
                owner=self.request.user
            ).annotate(
                latest_save_time=Subquery(latest_save_time_subquery)
            ).order_by('save_id', '-latest_save_time')

            # Serialize the data
            serialized = StateSaveSerializer(saved_state, many=True)
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


class GalleryView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (FormParser, JSONParser)
    methods = ['GET']

    @swagger_auto_schema(responses={200: GallerySerializer})
    def get(self, request):
        galleryset = Gallery.objects.filter()
        try:
            serialized = GallerySerializer(galleryset, many=True)
            return Response(serialized.data)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GalleryFetchSaveDeleteView(APIView):

    """
    Returns Saved data for given save id,
    Only staff can add / delete it
    THIS WILL ESCAPE DOUBLE QUOTES

    """
    # permission_classes = (AllowAny,)
    parser_classes = (FormParser, JSONParser)
    methods = ['GET']

    def is_owner(self):
        if not (self.request.user and self.request.user.is_authenticated):
            return False

        # Checking user roles
        userRoles = self.request.user.groups.all()
        for userRole in userRoles:
            if userRole.customgroup and userRole.customgroup.is_type_staff:
                return True

        return False

    @swagger_auto_schema(responses={200: GallerySerializer})
    def get(self, request, save_id):

        try:
            saved_state = Gallery.objects.get(
                save_id=save_id)
        except Gallery.DoesNotExist:
            return Response({'error': 'Does not Exist'},
                            status=status.HTTP_404_NOT_FOUND)
        try:
            serialized = GallerySerializer(
                saved_state, context={'request': request})
            data = {}
            data.update(serialized.data)
            return Response(data)
        except Exception:
            traceback.print_exc()
            return Response({'error': 'Not Able To Serialize'},
                            status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: GallerySerializer})
    def post(self, request, save_id):
        if not self.is_owner():
            return Response({'error': 'Not the owner'},
                            status=status.HTTP_401_UNAUTHORIZED)
        saved_state = Gallery()
        data = request.data
        if not (data['data_dump'] and data['media'] and data['save_id']):
            return Response({'error': 'not a valid POST request'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

        # saves to gallery
        try:
            saved_state.save_id = data.get('save_id')
            saved_state.data_dump = data.get('data_dump')
            if 'shared' in data:
                saved_state.shared = bool(data['shared'])
            saved_state.name = data.get('name')
            saved_state.description = data.get('description')
            if 'media' in data:
                img = Base64ImageField(max_length=None, use_url=True)
                filename, content = img.update(data['media'])
                saved_state.media.save(filename, content)
            saved_state.save()
            serialized = GallerySerializer(saved_state)
            return Response(serialized.data)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(responses={200: GallerySerializer})
    def delete(self, request, save_id):
        try:
            if not self.is_owner():
                return Response({'error': 'Not the owner'},
                                status=status.HTTP_401_UNAUTHORIZED)
            # Deltes from gallery
            try:
                saved_state = Gallery.objects.get(save_id=save_id)
            except Gallery.DoesNotExist:
                return Response({'error': 'Does not Exist'},
                                status=status.HTTP_404_NOT_FOUND)
            saved_state.delete()
            return Response({'done': True})
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
