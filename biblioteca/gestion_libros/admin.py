from django.contrib import admin
from .models import Libro, Prestamo, Usuario

admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(Usuario)
