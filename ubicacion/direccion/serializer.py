from rest_framework import serializers
from direccion.models import Direccion

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['id', 'continente', 'pais', 'region', 'ciudad','direccion','latitud','longitud']