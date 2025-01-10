from rest_framework import generics
from .models import EspacioDeportivo
from .serializers import EspacioDeportivoSerializer

class EspacioDeportivoListCreateAPIView(generics.ListCreateAPIView):
    queryset = EspacioDeportivo.objects.all()
    serializer_class = EspacioDeportivoSerializer

class EspacioDeportivoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EspacioDeportivo.objects.all()
    serializer_class = EspacioDeportivoSerializer
