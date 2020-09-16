from django.urls import path
from .views import *

app_name = "setlisttrackerapp"

urlpatterns = [
    path('', home, name='home'),
    path('songs/', song_list, name='songs'),
    path('events/', event_list, name='events')
]
