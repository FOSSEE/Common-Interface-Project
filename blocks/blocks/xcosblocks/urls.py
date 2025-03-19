from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CategoryViewSet, \
    NewBlockViewSet, NewBlockParameterViewSet, \
    get_block_images, set_block_parameter

router = SimpleRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'newblocks', NewBlockViewSet)
router.register(r'newblockparameters', NewBlockParameterViewSet)

urlpatterns = router.urls + [
    path(r'block_images', get_block_images),

    path(r'setblockparameter', set_block_parameter),
]
