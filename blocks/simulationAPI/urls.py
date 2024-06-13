from django.urls import path
from simulationAPI import views as simulationAPI_views


urlpatterns = [
    path('upload', simulationAPI_views.XmlUploader.as_view(),
         name='xmlUploader'),

    path('save', simulationAPI_views.XmlSave.as_view(),
         name='xmlSave'),

    path('status/<uuid:task_id>',
         simulationAPI_views.CeleryResultView.as_view(), name='celery_status'),

    path('streaming/<uuid:task_id>',
         simulationAPI_views.StreamView.as_view(), name='stream_status'),
]
