from rest_framework import serializers
from .models import EspacioDeportivo

class EspacioDeportivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspacioDeportivo
        fields = '__all__'
