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


@receiver(post_save, sender= AbstractUser)
def assign_user_permissions(sender, instance, created, **kwargs):
    if created:
        # Obtener el content type para el modelo Area
        area_content_type = ContentType.objects.get_for_model(Area)

        if instance.user_type == 1:  # Si es gerente
            # Asignar todos los permisos de áreas
            permissions = Permission.objects.filter(content_type=area_content_type)
            for permission in permissions:
                instance.user_permissions.add(permission)
        else:  # Si es usuario normal
            # Solo puede ver sus propias áreas
            view_permission = Permission.objects.get(
                codename='view_area',
                content_type=area_content_type
            )
            instance.user_permissions.add(view_permission)

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

