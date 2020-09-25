from django.urls import path
from simulationAPI import views as simulationAPI_views


urlpatterns = [
    path('upload', simulationAPI_views.XmlUploader.as_view(),
         name='xmlUploader'),

    path('status/<uuid:task_id>',
         simulationAPI_views.CeleryResultView.as_view(), name='celery_status'),

]
