from django import forms
from .models import Publication, Comment

class PublicationForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': '¿Qué estás pensando?',
            'rows': '3'
        }),
        label=''
    )

    class Meta:
        model = Publication
        fields = ['content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe un comentario...',
            'rows': '2'
        }),
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']
