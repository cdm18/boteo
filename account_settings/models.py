from django.db import models
from django.conf import settings
from reservations.models import Reservation

def user_profile_picture_path(instance, filename):
    return f'user_profile_pictures/{instance.user.id}/{filename}'

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to=user_profile_picture_path,
        default='default_profile.png',
        verbose_name="Foto de perfil"
    )
    about_me = models.TextField(verbose_name="Sobre mí", blank=True)

    def __str__(self):
        return f"Perfil de {self.user.email}"

    def save(self, *args, **kwargs):
        if not self.about_me:
            self.about_me = "Apasionado por el deporte y siempre buscando nuevas metas. ¡Vamos por más!"
        super().save(*args, **kwargs)
