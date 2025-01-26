from django import forms
from datetime import time, datetime, timedelta
from decimal import Decimal
from .models import Reservation
from django.forms import Select


class ExactHourWidget(Select):
    def __init__(self, *args, **kwargs):
        hours = [(f"{h}:00", f"{h}:00") for h in range(0, 24)]  # Opciones de 00:00 a 23:00
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

        # Validación de campos obligatorios
        if not space or not date or not start_time or not end_time:
            raise forms.ValidationError("Todos los campos son obligatorios.")

        # Validar que las horas sean exactas
        if start_time.minute != 0 or end_time.minute != 0:
            raise forms.ValidationError("Las horas deben ser exactas (por ejemplo, 13:00, 14:00).")

        # Validación de fechas pasadas
        today = datetime.now().date()
        if date < today:
            raise forms.ValidationError("No se puede reservar en fechas pasadas.")

        # Validación de horas pasadas en el día actual
        if date == today:
            current_time = datetime.now().time()
            if start_time < current_time:
                raise forms.ValidationError("No se puede reservar en horas pasadas del día actual.")

        # Validación de rango de horas
        if start_time >= end_time:
            raise forms.ValidationError("La hora de inicio debe ser anterior a la hora de fin.")

        # Validar que la duración sea un múltiplo de una hora
        duration_in_seconds = (
                datetime.combine(datetime.min, end_time) - datetime.combine(datetime.min, start_time)
        ).seconds
        if duration_in_seconds % 3600 != 0:
            raise forms.ValidationError("La duración debe ser un múltiplo exacto de una hora.")

        # Obtener el área asociada al espacio
        area = space.area

        # Verificar que las horas estén dentro del horario de apertura y cierre del área
        if start_time < area.opening_time or end_time > area.closing_time:
            raise forms.ValidationError(
                f"El horario de este espacio es: {area.opening_time} - {area.closing_time}."
            )

        # Validar conflictos de horario
        overlapping_reservations = Reservation.objects.filter(
            space=space,
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time,
        )
        if overlapping_reservations.exists():
            raise forms.ValidationError("Ya existe una reserva para este espacio en el horario seleccionado.")

        return cleaned_data
