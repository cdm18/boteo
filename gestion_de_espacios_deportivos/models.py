from django.db import models

class EspacioDeportivo(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    capacidad = models.IntegerField()
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
