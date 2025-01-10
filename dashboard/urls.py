from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
    def get(self, request):
        return Response({
            "message": "Bienvenido a Boteo API",
            "endpoints": {
                "dashboard": "/api/dashboard/overview/",
                "reservas": "/api/reservas/",
                "clientes": "/api/clientes/",
                "espacios": "/api/espacios/"
            }
        })

class OverviewAPIView(APIView):
    def get(self, request):
        api_urls = {
            'Dashboard': '/api/dashboard/overview/',
            'Reservas': '/api/reservas/',
            'Clientes': '/api/clientes/',
            'Espacios Deportivos': '/api/espacios/'
        }
        return Response(api_urls)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('overview/', OverviewAPIView.as_view(), name='overview'),
]