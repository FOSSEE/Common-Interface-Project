from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'blocks', views.BlockViewSet, basename='block')
urlpatterns = router.urls
