from django.urls import path
from .views import *

app_name = "setlisttrackerapp"

urlpatterns = [
    path('songs/', song_list, name='songs')
]
