from django.urls import path
from .views import convert_playlist

urlpatterns = [
    path('convert/', convert_playlist),
]
