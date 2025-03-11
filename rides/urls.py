from django.urls import path
from .views import create_ride, map_view

urlpatterns = [
    path('', map_view, name='home'),
    path('create_ride/', create_ride, name='create_ride'),
]

