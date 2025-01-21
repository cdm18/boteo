# forms.py
from django import forms
from django.core.exceptions import ValidationError

from .models import Area


class AreaCreationForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'description', 'address', 'city', 'opening_time',
                  'closing_time', 'has_parking', 'has_showers', 'has_lockers',
                  'has_equipment', 'images']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'opening_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
            }),
            'closing_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,

            }),
            'city': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe la descripción aquí...',
            }),
            'has_parking': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'has_lockers': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'has_showers': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'has_equipment': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'images': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'type': 'file',
            })
        }

        labels = {
            'opening_time': 'Hora de Apertura',
            'closing_time': 'Hora de Cierre',
            'name': 'Nombre',
            'description': 'Descripción',
            'address': 'Dirección',
            'city': 'Ciudad',
            'has_parking': 'Estacionamiento',
            'has_lockers': 'Casilleros',
            'has_showers': 'Duchas',
            'has_equipment': 'Equipamiento',
            'images': 'Imágenes'
        }

        error_messages = {
            'opening_time': {
                'required': 'La hora de apertura es obligatoria',
                'invalid': 'Formato de hora inválido'
            },
            'closing_time': {
                'required': 'La hora de cierre es obligatoria',
                'invalid': 'Formato de hora inválido'
            },
            'name': {
                'required': 'El nombre es obligatorio'
            },
            'description': {
                'required': 'El nombre es obligatorio'
            },
            'address': {
                'required': 'El nombre es obligatorio'
            },
            'city': {
                'required': 'El nombre es obligatorio'
            },
            'images': {
                'required': 'El nombre es obligatorio',
                'invalid': 'El archivo subido no es una imagen o está corrupto'
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        opening_time = cleaned_data.get('opening_time')
        closing_time = cleaned_data.get('closing_time')

        if opening_time and closing_time:
            if opening_time == closing_time:
                self.add_error('opening_time', 'La hora de apertura no puede ser igual a la hora de cierre')
                self.add_error('closing_time', 'La hora de cierre no puede ser igual a la hora de apertura')

            if opening_time > closing_time:
                self.add_error('opening_time', 'La hora de apertura debe ser anterior a la hora de cierre')
                self.add_error('closing_time', 'La hora de cierre debe ser posterior a la hora de apertura')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].widget.initial_text = "Actual"
        self.fields['images'].widget.clear_checkbox_label = "Eliminar"
        self.fields['images'].widget.input_text = "Cambiar"
