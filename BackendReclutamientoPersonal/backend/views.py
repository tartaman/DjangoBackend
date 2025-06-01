from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
#serializers
from .serializers import CustomTokenObtainPairSerializer
from .serializers import UsuarioSerializer
from .serializers import VacanteSerializer
from .serializers import SolicitudSerializer
#rest_framework imports
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializers import UsuarioSerializer
# for knowing if the user is authenticated
from rest_framework.permissions import IsAuthenticated
from .models import Usuario
from .models import Vacante
from .models import Solicitud
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
        
# A view, to handle the APIRestful for Vacantes
class VacanteViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Vacantes.
    """
    queryset = Vacante.objects.all()  # Uncomment this when you have the Vacante model
    # serializer_class = VacanteSerializer  # Uncomment this when you have the Vacante serializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    def get_queryset(self):
        return Vacante.objects.filter(activa=True)  # Only return active vacancies
    
class SolicitudViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Solicitudes.
    """
    queryset = Solicitud.objects.all()  # Uncomment this when you have the Solicitud model
    # serializer_class = SolicitudSerializer  # Uncomment this when you have the Solicitud serializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    
    def get_queryset(self):
        return Solicitud.objects.filter(usuario=self.request.user)  # Only return solicitudes for the authenticated user