from django.db import models
from django.conf import settings
from reservations.models import Reservation


class Bill(models.Model):
    BILL_STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('paid', 'Pagada'),
        ('rejected', 'Rechazada')
    ]

    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name='bills'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(max_length=200)
    identification = models.CharField(max_length=10, blank=True, null=True)
    space_name = models.CharField(max_length=200)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=BILL_STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Factura {self.id}: {self.full_name} - {self.space_name} - {self.status}"
