from django.db import models
from users.models import CustomUser


class Publication(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.created_at.strftime("%d/%m/%Y")}'

class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

class Like(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('publication', 'user')
