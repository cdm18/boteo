from django.urls import path  # Importa la función 'path' para definir las URLs
from publications import views  # Importa las vistas del archivo 'views.py'

# Define el nombre de la aplicación (namespace) para las URLs
app_name = 'publications'

# Lista de URLs para la aplicación 'publications'
urlpatterns = [
    # Ruta para la vista de la lista de publicaciones
    path('', views.publication_list, name='publication_list'),  # Cuando la URL sea '/', se llama a la vista 'publication_list'
]
