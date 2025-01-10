from django import forms
from .models import SportsSpace, Area

class SportsSpaceForm(forms.ModelForm):
    class Meta:
        model = SportsSpace
        fields = ['name', 'description', 'address', 'city', 'opening_hours', 'closing_hours', 'general_services', 'images']

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'sport_type', 'area_description', 'space']
