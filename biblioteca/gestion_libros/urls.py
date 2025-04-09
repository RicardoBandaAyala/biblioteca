from django.urls import path
from django.contrib.auth import views as auth_views
from .views import listar_libros, registrar_libro, prestar_libro, devolver_libro, listar_usuarios, apartar_libro, desapartar_libro, perfil, registrar_usuario

urlpatterns = [
    path('', listar_libros, name='listar_libros'),
    path('registrar/', registrar_libro, name='registrar_libro'),
    path('prestar/<int:libro_id>/', prestar_libro, name='prestar_libro'),
    path('devolver/<int:prestamo_id>/', devolver_libro, name='devolver_libro'),
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('apartar/<int:libro_id>/', apartar_libro, name='apartar_libro'),
    path('desapartar/<int:libro_id>/', desapartar_libro, name='desapartar_libro'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Agrega esta línea para el inicio de sesión
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Opcional: para cerrar sesión
    path('perfil/', perfil, name='perfil'),  # Agrega esta línea para el formulario de contacto
    path('registrar_usuario/', registrar_usuario, name='registrar_usuario'), # Agrega esta línea para el formulario de registrarse
]
