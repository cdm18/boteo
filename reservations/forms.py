from django import forms
from datetime import time, datetime, timedelta
from decimal import Decimal
from .models import Reservation
from django.forms import Select

from django import forms
from datetime import time, datetime, timedelta
from decimal import Decimal
from django.forms import Select
from django.db import models

class ExactHourWidget(Select):
    def __init__(self, *args, **kwargs):
        hours = [(f"{h:02d}:00", f"{h:02d}:00") for h in range(0, 24)]
        super().__init__(choices=hours, *args, **kwargs)

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['space', 'date', 'start_time', 'end_time']
        widgets = {
            'space': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': ExactHourWidget(attrs={'class': 'form-control'}),
            'end_time': ExactHourWidget(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        space = cleaned_data.get('space')
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if not all([space, date, start_time, end_time]):
            raise forms.ValidationError("Todos los campos son obligatorios.")

        # Validar horas exactas
        if any(time.minute != 0 for time in [start_time, end_time]):
            raise forms.ValidationError("Las horas deben ser exactas (por ejemplo, 13:00, 14:00).")

        # Validar fechas pasadas
        today = datetime.now().date()
        if date < today:
            raise forms.ValidationError("No se puede reservar en fechas pasadas.")

        # Validar horas pasadas en el día actual
        if date == today and start_time < datetime.now().time():
            raise forms.ValidationError("No se puede reservar en horas pasadas del día actual.")

        # Validar rango de horas
        if start_time >= end_time:
            raise forms.ValidationError("La hora de inicio debe ser anterior a la hora de fin.")

        # Validar duración en horas exactas
        duration = (datetime.combine(date, end_time) - datetime.combine(date, start_time)).seconds
        if duration % 3600 != 0:
            raise forms.ValidationError("La duración debe ser un múltiplo exacto de una hora.")

        # Validar horario del área
        area = space.area
        if start_time < area.opening_time or end_time > area.closing_time:
            raise forms.ValidationError(
                f"El horario de este espacio es: {area.opening_time} - {area.closing_time}."
            )

        # Validar conflictos de horario
        if space and date and start_time and end_time:
            overlapping_reservations = Reservation.objects.filter(
                space=space,
                date=date,
                status__in=['Pendiente', 'Confirmado']
            ).filter(
                models.Q(start_time__lt=end_time, end_time__gt=start_time) |
                models.Q(start_time=start_time, end_time=end_time)
            )

            if self.instance.pk:
                overlapping_reservations = overlapping_reservations.exclude(pk=self.instance.pk)

            if overlapping_reservations.exists():
                raise forms.ValidationError(
                    "Ya existe una reserva para este espacio en el horario seleccionado o hay un conflicto de horarios."
                )

        return cleaned_data