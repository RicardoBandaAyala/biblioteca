from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Prestamo, Libro, Usuario

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero', 'isbn', 'disponible']

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'correo', 'password1', 'password2']  # Campos que se mostrarán en el formulario
