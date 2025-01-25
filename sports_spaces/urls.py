from django.urls import path
from .views import sport_space_detail_view, create_space_view

urlpatterns = [
    path('sport_spaces/<int:pk>', sport_space_detail_view, name='sport_space_detail'),
    path('<int:pk>/create_space/', create_space_view, name='create_sport_space'),
]
