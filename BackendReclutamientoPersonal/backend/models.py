from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('El campo "username" es obligatorio')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)  # nombre de usuario
    email = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'  # Esto le dice a Django qué campo usar para login
    REQUIRED_FIELDS = []  # campos requeridos al crear superusuario

    def __str__(self):
        return self.username

class Vacante(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre de la vacante (ej. 'Backend Developer')
    puesto = models.CharField(max_length=100)  # Área o departamento (ej. 'Tecnología')
    descripcion = models.TextField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)  # Para ocultar vacantes antiguas

class Solicitud(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    mensaje = models.TextField(blank=True, null=True)  # Mensaje opcional del postulante
    estado = models.CharField(max_length=50, default='Pendiente')  # Pendiente, Aceptado, Rechazado, etc.

