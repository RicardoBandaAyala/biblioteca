from django.db import models
from django.contrib.auth.models import AbstractUser

#Modelo para Usuarios
class Usuario(AbstractUser):
    correo = models.EmailField(unique=True)
    libros_prestados = models.ManyToManyField('Libro', blank=True)

#Modelo para Libros
class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
#Modelo para los Prestamos
class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.libro.titulo}'

# Create your models here.
