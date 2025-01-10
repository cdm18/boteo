from django.urls import path
from .views import ReservaListCreateAPIView, ReservaDetailAPIView

urlpatterns = [
    path('', ReservaListCreateAPIView.as_view(), name='reservas-list'),
    path('<int:pk>/', ReservaDetailAPIView.as_view(), name='reservas-detail'),
]
