from django.urls import path
from account_settings.views import *

# Definir el namespace para las URLs de account_settings
app_name = 'account_settings'

urlpatterns = [
    path('', profile_view, name='profile'),  # Ruta para el perfil
    path('edit-profile/', edit_profile, name='edit_profile'),  # Ruta para editar el perfil
]
