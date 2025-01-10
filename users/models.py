from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Nombre de usuario",
        null=True,
        blank=True
    )

    USERNAME_FIELD = 'email'  # Email como identificador principal
    REQUIRED_FIELDS = ['username']  # Username será obligatorio además del email

    def __str__(self):
        return self.email
