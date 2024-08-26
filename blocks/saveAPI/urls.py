from django.urls import path
from saveAPI import views as saveAPI_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'save/search', saveAPI_views.SaveSearchViewSet,
                basename='SaveSearch')

urlpatterns = [
    path('save', saveAPI_views.StateSaveView.as_view(),
         name='saveState'),

    path('save/list', saveAPI_views.UserSavesView.as_view(),
         name='listSaves'),

    path("save/gallery", saveAPI_views.GalleryView.as_view(),
         name="getGallery"),

    path('save/gallery/<str:save_id>',
         saveAPI_views.GalleryFetchSaveDeleteView.as_view(),
         name='fetchGallerySchematic'),

    path("save/<uuid:save_id>", saveAPI_views.DeleteDiagram.as_view(),
         name="deleteDiagram"),

]

urlpatterns += router.urls
