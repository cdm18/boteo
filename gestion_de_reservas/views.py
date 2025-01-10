from rest_framework import generics
from .models import Reserva
from .serializers import ReservaSerializer

class ReservaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
