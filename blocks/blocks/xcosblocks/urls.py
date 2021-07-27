from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, BlockViewSet, BlockParameterViewSet, \
    set_block_parameter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'blocks', BlockViewSet)
router.register(r'block_parameters', BlockParameterViewSet)
urlpatterns = router.urls
urlpatterns += [
    path('setblockparameter', set_block_parameter),
]
