from django.urls import path
from . import views

urlpatterns = [
    path('', views.speech_recognition_view, name='speech_recognition'),
]
