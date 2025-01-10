from django.urls import path
from .views import ClienteListCreateAPIView, ClienteDetailAPIView
from .views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path('', ClienteListCreateAPIView.as_view(), name='clientes-list'),
    path('<int:pk>/', ClienteDetailAPIView.as_view(), name='clientes-detail'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
