from django.urls import path
from account_settings.views import *

app_name = 'account_settings'

urlpatterns = [
    path('', profile_view, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
]
