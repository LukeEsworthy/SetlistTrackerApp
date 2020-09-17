from django.urls import include, path
from .views import *

app_name = "setlisttrackerapp"

urlpatterns = [
    path('', home, name='home'),
    path('songs/', song_list, name='songs'),
    path('song/form', song_form, name='song_form'),
    path('events/', event_list, name='events'),
    path('event/form', event_form, name='event_form'),
    path('events/<int:event_id>/', event_details, name='event'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
]
