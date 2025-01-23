from django.db import models
from users.models import CustomUser  # Importamos el modelo CustomUser, que representa a los usuarios


# Modelo para las publicaciones
class Publication(models.Model):
    # Relación de la publicación con un usuario (usuario que creó la publicación)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # Campo de texto para el contenido de la publicación
    content = models.TextField()

    # Campos para las fechas de creación y actualización de la publicación
    created_at = models.DateTimeField(auto_now_add=True)  # Se establece automáticamente cuando se crea la publicación
    updated_at = models.DateTimeField(auto_now=True)  # Se actualiza automáticamente cada vez que se modifica

    class Meta:
        # Ordenar las publicaciones por fecha de creación, de más reciente a más antiguo
        ordering = ['-created_at']

        # Establecer nombres amigables para el modelo
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    # Método que devuelve una representación legible de la publicación
    def __str__(self):
        # Se muestra el nombre completo del usuario y la fecha de creación de la publicación
        return f'{self.user.get_full_name()} - {self.created_at.strftime("%d/%m/%Y")}'


# Modelo para los comentarios
class Comment(models.Model):
    # Relación del comentario con la publicación a la que pertenece
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')

    # Relación del comentario con el usuario que lo creó
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # Campo de texto para el contenido del comentario
    content = models.TextField()

    # Fecha de creación del comentario
    created_at = models.DateTimeField(auto_now_add=True)  # Se establece automáticamente cuando se crea el comentario

    class Meta:
        # Ordenar los comentarios por fecha de creación, de más antiguo a más reciente
        ordering = ['created_at']

        # Establecer nombres amigables para el modelo
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"


# Modelo para los likes (me gusta)
class Like(models.Model):
    # Relación del like con la publicación a la que pertenece
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='likes')

    # Relación del like con el usuario que lo dio
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # Fecha de creación del like
    created_at = models.DateTimeField(auto_now_add=True)  # Se establece automáticamente cuando se da el like

    class Meta:
        # Aseguramos que un usuario no pueda dar más de un like a la misma publicación
        unique_together = ('publication', 'user')  # Restricción única de usuario por publicación
