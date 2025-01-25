from django import forms
from .models import SportsSpace


class SportsSpaceForm(forms.ModelForm):
    class Meta:
        model = SportsSpace
        fields = ['name', 'sport_type', 'length', 'width', 'surface', 'recommended_capacity', 'cost_per_hour']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'}),
            'sport_type': forms.Select(choices=SportsSpace.SPORTS_TYPES, attrs={
                'class': 'form-control'}),
            'length': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'decimal',
                'min': '1'}),
            'width': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'decimal',
                'min': '1'
            }),
            'surface': forms.Select(choices=SportsSpace.SURFACE_TYPES, attrs={
                'class': 'form-control'}),
            'recommended_capacity': forms.NumberInput(attrs={
                'class': 'form-control'}),
            'cost_per_hour': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'decimal',
                'min': '1'
            })
        }
