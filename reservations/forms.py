from .models import Reservation
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['space', 'date', 'start_time', 'end_time']
        widgets = {
            'space': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        date = cleaned_data.get('date')
        space = cleaned_data.get('space')

        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("La hora de inicio debe ser anterior a la hora de fin.")

        overlapping_reservations = Reservation.objects.filter(
            space=space,
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time
        )

        if overlapping_reservations.exists():
            raise forms.ValidationError("Ya existe una reserva para este horario y espacio.")

        return cleaned_data