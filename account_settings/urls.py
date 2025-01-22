from django.urls import path
from . import views

app_name = 'account_settings'

urlpatterns = [
    path('', views.profile_view, name='profile'),  # Esta será la URL /account/
    path('edit/', views.edit_profile, name='edit_profile'),  # Esta será /account/edit/
]