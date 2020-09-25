from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "setlisttrackerapp"

urlpatterns = [
    path('', home, name='home'),
    path('landingpage', landing_page, name='landing'),
    path('songs/', song_list, name='songs'),
    path('song/form', song_form, name='song_form'),
    path('song/search', song_list_search, name='search_songs'),
    path('events/', event_list, name='events'),
    path('event/form', event_form, name='event_form'),
    path('events/<int:event_id>/', event_details, name='event'),
    path('events/<int:event_id>/form/', event_edit_form, name='event_edit_form'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name="register"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
