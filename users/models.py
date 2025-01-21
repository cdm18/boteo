from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Permission
from areas.models import Area
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from areas.models import Area


class CustomUser(AbstractUser):
    USER_TYPES = [
        (0, 'Usuario Normal'),
        (1, 'Gerente'),
    ]
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Nombre de usuario",
        null=True,
        blank=True
    )
    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPES,
        default=0,
        verbose_name="Tipo de Usuario"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.email

