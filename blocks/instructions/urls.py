from django.urls import path
from instructions import views as instructions_views


urlpatterns = [
    path('get', instructions_views.Instructions.as_view(),
         name='instructions')
]
