# forms.py
from django import forms
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].widget.initial_text = "Actual"
        self.fields['images'].widget.clear_checkbox_label = "Eliminar"
        self.fields['images'].widget.input_text = "Cambiar"
