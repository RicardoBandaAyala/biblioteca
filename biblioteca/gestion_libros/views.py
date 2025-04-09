from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Prestamo, Usuario
from .forms import PrestamoForm, LibroForm, RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Para mostrar mensajes al usuario

# Vistas para gestionar libros y usuarios
def listar_libros(request):
    libros = Libro.objects.all()
    query = request.GET.get('q')
    if query:
        libros = libros.filter(titulo__icontains=query)
    return render(request, 'libros/listar_libros.html', {'libros': libros, 'query': query})

# Vista para registrar un nuevo libro
@login_required                                        #Solo permitir si se esta registrado
def registrar_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/registrar_libro.html', {'form': form})

# Vista para pedir prestado un libro existente
@login_required
def prestar_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    if libro.disponible and request.user.libros_prestados.count() < 3:
        prestamo = Prestamo.objects.create(usuario=request.user, libro=libro)
        libro.disponible = False
        libro.save()
        request.user.libros_prestados.add(libro)
    return redirect('listar_libros')

# Vista para devolver un libro existente
@login_required
def devolver_libro(request, prestamo_id):
    prestamo = Prestamo.objects.get(id=prestamo_id)
    prestamo.libro.disponible = True
    prestamo.libro.save()
    request.user.libros_prestados.remove(prestamo.libro)
    prestamo.delete()
    return redirect('listar_libros')

# Vista para listar los usuarios registrados
@login_required
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})

# Vista para el boton apartar un libro
@login_required
def apartar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if not libro.disponible:  # Verifica si el libro ya está apartado
        messages.error(request, f'El libro "{libro.titulo}" ya está apartado por otro usuario.')
        return redirect('listar_libros')  # Redirige a la lista de libros con un mensaje de error

    # Si el libro está disponible, se aparta
    libro.disponible = False
    libro.save()
    messages.success(request, f'Has apartado el libro "{libro.titulo}".')
    return redirect('listar_libros')

# Vista para el boton devolver un libro
@login_required
def desapartar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if not libro.disponible:
        libro.disponible = True
        libro.save()
    return redirect('listar_libros')  # Redirige a la lista de libros

# Vista para el perfil del usuario
@login_required
def perfil(request):
    usuario = request.user  # Obtiene el usuario autenticado
    libros_prestados = usuario.libros_prestados.all()  # Obtiene los libros prestados por el usuario
    return render(request, 'usuarios/perfil.html', {
        'usuario': usuario,
        'libros_prestados': libros_prestados
    })

# Vista para registrar un nuevo usuario
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login después del registro
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registrar_usuario.html', {'form': form})