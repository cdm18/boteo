from django import forms
from django.core.exceptions import ValidationError
from .models import Publication, Comment

# Formulario para crear una publicación
class PublicationForm(forms.ModelForm):
    # Definimos el campo 'content' como un campo de texto (CharField)
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': '¿Qué estás pensando?',
            'rows': '2'
        }),
        label=''
    )

    class Meta:
        model = Publication
        fields = ['content']

    # Validación del contenido para que no exceda los 500 caracteres
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > 500:
            raise ValidationError('El texto no puede exceder los 500 caracteres.')
        return content


# Formulario para agregar un comentario
class CommentForm(forms.ModelForm):
    # Definimos el campo 'content' como un campo de texto (CharField)
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe un comentario...',
            'rows': '1'
        }),
        label=''
    )

    class Meta:
        # Le decimos a Django que este formulario está basado en el modelo Comment
        model = Comment
        # Especificamos qué campo(s) queremos incluir en el formulario (solo 'content' en este caso)
        fields = ['content']
