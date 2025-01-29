from django.db import models
from areas.models import Area


class SportsSpace(models.Model):
    name = models.CharField(max_length=100)

    SPORTS_TYPES = [
        ('Fútbol', 'Fútbol'),
        ('Basketball', 'Basketball'),
        ('Piscina', 'Piscina'),
        ('Gym', 'Gym'),
        ('Ecuavoley', 'Ecuavoley'),
    ]
    SURFACE_TYPES = [
        ("Sintética", "Sintética"),
        ("Pasto Natural", "Pasto Natural"),
        ("Cemento", "Cemento"),
        ("Piscina", "Piscina")
    ]

    sport_type = models.CharField(max_length=100, choices=SPORTS_TYPES, verbose_name="Tipo de Deporte",
                                  default=SPORTS_TYPES[0])
    length = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    width = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    surface = models.CharField(max_length=16, choices=SURFACE_TYPES, verbose_name="Tipo de Superficie",
                               default=SURFACE_TYPES[0][1])
    recommended_capacity = models.IntegerField(verbose_name="Capacidad", null=True, blank=True)
    cost_per_hour = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='css', null=True)

    def __str__(self):
        return f"{self.name} ({self.sport_type})"
