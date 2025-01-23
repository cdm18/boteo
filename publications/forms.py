from django import forms
from .models import Publication, Comment  # Importamos los modelos Publication y Comment

# Formulario para crear una publicación
class PublicationForm(forms.ModelForm):
    # Definimos el campo 'content' como un campo de texto (CharField)
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',  # Clase para el estilo del formulario (Bootstrap)
            'placeholder': '¿Qué estás pensando?',  # Texto de sugerencia dentro del campo
            'rows': '2'  # Número de filas (altura del área de texto)
        }),
        label=''  # No ponemos una etiqueta visible para el campo
    )

    class Meta:
        # Le decimos a Django que este formulario está basado en el modelo Publication
        model = Publication
        # Especificamos qué campo(s) queremos incluir en el formulario (solo 'content' en este caso)
        fields = ['content']


# Formulario para agregar un comentario
class CommentForm(forms.ModelForm):
    # Definimos el campo 'content' como un campo de texto (CharField)
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',  # Clase para el estilo del formulario (Bootstrap)
            'placeholder': 'Escribe un comentario...',  # Texto de sugerencia dentro del campo
            'rows': '1'  # Número de filas (altura del área de texto)
        }),
        label=''  # No ponemos una etiqueta visible para el campo
    )

    class Meta:
        # Le decimos a Django que este formulario está basado en el modelo Comment
        model = Comment
        # Especificamos qué campo(s) queremos incluir en el formulario (solo 'content' en este caso)
        fields = ['content']
