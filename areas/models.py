from django.db import models
from django.db.models import ForeignKey
from django.conf import settings
from users.models import CustomUser


# Create your models here.
class Area(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    city = models.TextField()
    opening_time = models.TimeField(verbose_name="Hora de Apertura")
    closing_time = models.TimeField(verbose_name="Hora de Cierre")
    has_parking = models.BooleanField(default=False)
    has_showers = models.BooleanField(default=False)
    has_lockers = models.BooleanField(default=False)
    has_equipment = models.BooleanField(default=False)
    images = models.ImageField(upload_to='area', verbose_name="Imágenes del Espacio", blank=True, null=True)

    def __str__(self):
        return self.name