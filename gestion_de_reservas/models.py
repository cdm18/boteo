from django.db import models

class Reserva(models.Model):
    cliente = models.ForeignKey('gestion_de_clientes.Cliente', on_delete=models.CASCADE)
    espacio_deportivo = models.ForeignKey('gestion_de_espacios_deportivos.EspacioDeportivo', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Confirmada', 'Confirmada'), ('Cancelada', 'Cancelada')])

    def __str__(self):
        return f"Reserva de {self.cliente} en {self.espacio_deportivo} el {self.fecha}"
