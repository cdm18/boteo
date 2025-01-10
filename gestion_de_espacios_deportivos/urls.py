from django.urls import path
from .views import EspacioDeportivoListCreateAPIView, EspacioDeportivoDetailAPIView

urlpatterns = [
    path('', EspacioDeportivoListCreateAPIView.as_view(), name='espacios-list'),
    path('<int:pk>/', EspacioDeportivoDetailAPIView.as_view(), name='espacios-detail'),
]
