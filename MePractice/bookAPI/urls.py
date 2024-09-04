from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.API_Home, name='home'),
]