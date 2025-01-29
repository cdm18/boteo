from django.db import models
from users.models import CustomUser  # Importamos el modelo CustomUser, que representa a los usuarios


# Modelo para las publicaciones
class Publication(models.Model):
    # Relación de la publicación con un usuario (usuario que creó la publicación)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"


# Modelo para los comentarios
class Comment(models.Model):
    # Relación del comentario con la publicación a la que pertenece
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')
    # Relación del comentario con el usuario que lo creó
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"


# Modelo para los likes (me gusta)
class Like(models.Model):
    # Relación del like con la publicación a la que pertenece
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='likes')
    # Relación del like con el usuario que lo dio
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Aseguramos que un usuario no pueda dar más de un like a la misma publicación
        unique_together = ('publication', 'user')  # Restricción única de usuario por publicación
