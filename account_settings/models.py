from django.db import models
from django.conf import settings

# Función para generar la ruta de la foto de perfil
def user_profile_picture_path(instance, filename):
    return f"profile_pictures/{instance.user.id}/{filename}"

# Modelo para el perfil del usuario
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to=user_profile_picture_path,
        verbose_name="Foto de perfil"
    )
    about_me = models.TextField(verbose_name="Sobre mí", blank=True)
    favorite_sports = models.CharField(max_length=255, verbose_name="Deportes favoritos", blank=True)
