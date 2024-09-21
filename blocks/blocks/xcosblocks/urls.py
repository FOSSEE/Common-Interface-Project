from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, \
    NewBlockViewSet, NewBlockParameterViewSet, \
    get_block_images, set_block_parameter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'newblocks', NewBlockViewSet)
router.register(r'newblockparameters', NewBlockParameterViewSet)
urlpatterns = router.urls
urlpatterns += [
    path(r'setblockparameter', set_block_parameter),
    path(r'block_images', get_block_images)
]
