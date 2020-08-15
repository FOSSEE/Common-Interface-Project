from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, BlockViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'blocks', BlockViewSet, basename='block')
urlpatterns = router.urls
