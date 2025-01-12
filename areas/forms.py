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
            'opening_time': forms.TimeInput(attrs={'type': 'time'}),
            'closing_time': forms.TimeInput(attrs={'type': 'time'}),
        }