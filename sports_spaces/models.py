from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class SportsSpace(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default='Loja')  # Añadimos default
    cost_per_hour = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0.00  # Añadimos default
    )
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )
    image = models.ImageField(upload_to='spaces/', null=True, blank=True)
    SPORTS_TYPES = [
        ('Fútbol', 'Fútbol'),
        ('Ecuavoley', 'Ecuavoley'),
        ('Piscina', 'Piscina'),
    ]
    sport_type = models.CharField(
        max_length=100, 
        choices=SPORTS_TYPES,
        default='Fútbol'  # Añadimos default
    )

    class Meta:
        ordering = ['-rating']

    def __str__(self):
        return self.name