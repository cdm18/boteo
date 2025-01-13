from django.db import models

# Create your models here.
class Pago(models.Model):
    cliente = models.CharField(max_length=100)
    correo = models.EmailField(null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(
        max_length=10,
        choices=[("Pendiente", "Pendiente"), ("Pagado", "Pagado")],
        default="Pendiente"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.cliente} - {self.monto}"
