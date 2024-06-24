from django.urls import path
from saveAPI import views as saveAPI_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'search', saveAPI_views.SaveSearchViewSet,
                basename='SaveSearch')

urlpatterns = [
    path('diagram', saveAPI_views.StateSaveView.as_view(),
         name='saveState'),

    path('list', saveAPI_views.UserSavesView.as_view(),
         name='listSaves'),

    path("gallery", saveAPI_views.GalleryView.as_view(),
         name="getGallery"),

    path('gallery/<str:save_id>',
         saveAPI_views.GalleryFetchSaveDeleteView.as_view(),
         name='fetchGallerySchematic'),

    path("diagram/<uuid:save_id>", saveAPI_views.FetchSaveDiagram.as_view(),
         name="getDiagram"),

]

urlpatterns += router.urls
