from rest_framework.views import APIView
from rest_framework.response import Response

class OverviewAPIView(APIView):
    def get(self, request):
        api_urls = {
            'Dashboard': '/api/dashboard/overview/',
            'Reservas': '/api/reservas/',
            'Clientes': '/api/clientes/',
            'Espacios Deportivos': '/api/espacios/'
        }
        return Response(api_urls)