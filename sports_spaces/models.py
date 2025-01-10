from django.db import models

class SportsSpace(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del Espacio Deportivo")
    description = models.TextField(verbose_name="Descripción", blank=True)
    address = models.CharField(max_length=255, verbose_name="Dirección")
    city = models.CharField(max_length=100, verbose_name="Ciudad")
    opening_time = models.TimeField(verbose_name="Hora de Apertura")
    closing_time = models.TimeField(verbose_name="Hora de Cierre")
    general_services = models.TextField(verbose_name="Servicios Generales", blank=True)
    images = models.ImageField(upload_to='sports_spaces/', verbose_name="Imágenes del Espacio", blank=True, null=True)

    def __str__(self):
        return self.name

class Area(models.Model):
    SPORTS_TYPES = [
        ('Fútbol', 'Fútbol'),
        ('Basketball', 'Basketball'),
        ('Piscina', 'Piscina'),
        ('Gym', 'Gym'),
        ('Ecuavoley', 'Ecuavoley'),
    ]

    sports_space = models.ForeignKey(SportsSpace, on_delete=models.CASCADE, related_name='areas')
    name = models.CharField(max_length=200, verbose_name="Nombre del Área")
    sport_type = models.CharField(max_length=100, choices=SPORTS_TYPES, verbose_name="Tipo de Deporte")
    capacity = models.IntegerField(verbose_name="Capacidad", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.sport_type})"
