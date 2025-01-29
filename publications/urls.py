from django.urls import path  # Importa la función 'path' para definir las URLs
from publications import views  # Importa las vistas del archivo 'views.py'

app_name = 'publications'

urlpatterns = [
    path('', views.publication_list, name='publication_list'),
]
