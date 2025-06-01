from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializers import UsuarioSerializer
from .models import Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Usuarios.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer  # Assuming you have a serializer named UsuarioSerializer


# Custom Token Obtain Pair View
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("Datos recibidos:", request.data)
        usuario = request.data.get('usuario')
        password = request.data.get('password')

        if not usuario or not password:
            return Response({'error': 'Usuario y contraseña son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=usuario, password=password)

        if user is not None:
            return Response({'message': 'Login exitoso', 'id': user.id})
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)