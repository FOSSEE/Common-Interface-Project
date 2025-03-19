from django.urls import path
from saveAPI import views as saveAPI_views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'search', saveAPI_views.SaveSearchViewSet, basename='SaveSearch')

urlpatterns = router.urls + [
    path('categories', saveAPI_views.BookCategoryView.as_view(), name='categories'),
    path('books', saveAPI_views.BookView.as_view(), name='books'),
    path("gallery", saveAPI_views.GalleryListView.as_view(), name="getGallery"),
    path('gallery/<str:save_id>', saveAPI_views.GalleryDetailView.as_view(), name='fetchGallerySchematic'),

    path('list', saveAPI_views.UserSavesView.as_view(), name='listSaves'),
    path('diagram', saveAPI_views.StateSaveView.as_view(), name='saveState'),
    path("diagram/<uuid:save_id>", saveAPI_views.FetchSaveDiagram.as_view(), name="getDiagram"),
]
