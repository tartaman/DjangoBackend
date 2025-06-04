from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, LoginView
from .views import CustomTokenObtainPairView
from .views import VacanteViewSet
from .views import SolicitudViewSet
router = DefaultRouter()

#register the viewset with the router
# This will automatically create the necessary routes for the UsuarioViewSet
router.register(r'usuarios', UsuarioViewSet)
router.register(r'vacantes', VacanteViewSet)
router.register(r'solicitudes', SolicitudViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomTokenObtainPairView.as_view(), name='tokenPairview'),  # Login
]
