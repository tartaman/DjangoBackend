from rest_framework import serializers
from .models import Usuario


#Serializer para el modelo Usuario (para endpoints restful)
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  # Serializa todos los campos del modelo Usuario