from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Usuario
from .models import Vacante
from .models import Solicitud

#Serializer para el modelo Usuario (para endpoints restful)
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')  # sacar la contraseña
        user = Usuario(**validated_data)
        user.set_password(password)  # aquí se hashea
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        return data

# Serializer for the Vacante model 
class VacanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacante  # Assuming you have a Vacante model
        fields = '__all__'  # Adjust fields as necessary

# Serializer for the Solicitud model
class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud  # Assuming you have a Solicitud model
        fields = '__all__'  # Adjust fields as necessary