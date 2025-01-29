from django import forms
from account_settings.models import UserProfile

# Formulario para actualizar el perfil del usuario
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'about_me', 'favorite_sports']
        widgets = {
            'about_me': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Cuéntanos sobre ti...'
            }),
            'favorite_sports': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Fútbol, Vóley'
            })
        }
