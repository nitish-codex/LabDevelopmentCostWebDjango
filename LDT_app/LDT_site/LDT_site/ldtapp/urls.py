from django.urls import path

from . import views

urlpatterns = [
    path('', views.costAnalysis, name='costAnalysis'),
]