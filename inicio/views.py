from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Libro, Socio, Prestamo
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy



def inicio(request):
    return render(request, "inicio/inicio.html")

@login_required
def crear_libro2(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        fecha_publicacion = request.POST.get("fecha_publicacion")
        cantidad = request.POST.get("cantidad")
        isbn = request.POST.get("isbn")

        libro = Libro(
            titulo=titulo,
            autor=autor,
            fecha_publicacion=fecha_publicacion,
            cantidad=cantidad,
            isbn=isbn
        )
        libro.save()
        return HttpResponse(f"Libro '{titulo}' creado con éxito.")

    return render(request, "inicio/crear_libro2.html")

def listar_libros(request):
    query = request.GET.get("q")
    if query:
        libros = Libro.objects.filter(titulo__icontains=query) | Libro.objects.filter(autor__icontains=query)
    else:
        libros = Libro.objects.all()
    return render(request, "inicio/listar_libros.html", {"libros": libros})

def crear_socio(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        grado = request.POST.get("grado")
        socio = Socio(nombre=nombre, apellido=apellido, grado=grado)
        socio.save()
        return HttpResponse(f"Socio {nombre} {apellido} creado con éxito.")
    return render(request, "inicio/crear_socio.html")

def listar_socios(request):
    q = request.GET.get("q", "")
    if q:
        socios = Socio.objects.filter(nombre__icontains=q) | Socio.objects.filter(apellido__icontains=q)
    else:
        socios = Socio.objects.all()
    return render(request, "inicio/listar_socios.html", {"socios": socios})

def crear_prestamo(request):
    if request.method == "POST":
        socio_id = request.POST.get("socio")
        libro_id = request.POST.get("libro")
        socio = Socio.objects.get(id=socio_id)
        libro = Libro.objects.get(id=libro_id)
        prestamo = Prestamo(socio=socio, libro=libro)
        prestamo.save()
        return HttpResponse(f"Su préstamo fue registrado: {socio} → {libro}")

    socios = Socio.objects.all()
    libros = Libro.objects.all()
    return render(request, "inicio/crear_prestamo.html", {"socios": socios, "libros": libros})

def listar_prestamos(request):
    q = request.GET.get("q", "")
    prestamos = Prestamo.objects.select_related("socio", "libro").all()
    if q:
        prestamos = prestamos.filter(
            Q(socio__nombre__icontains=q) |
            Q(socio__apellido__icontains=q) |
            Q(libro__titulo__icontains=q) |
            Q(libro__autor__icontains=q)
        )
    return render(request, "inicio/listar_prestamos.html", {"prestamos": prestamos, "q": q})

def acerca_de_mi(request):
    return render(request, "inicio/acerca.html")



class LibroListView(LoginRequiredMixin, ListView):
    model = Libro
    template_name = "inicio/listar_libros_cbv.html"
    context_object_name = "libros"

class LibroDetailView(LoginRequiredMixin, DetailView):
    model = Libro
    template_name = "inicio/detalle_libro.html"
    context_object_name = "libro"

class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    template_name = "inicio/crear_libro_cbv.html"
    fields = ["titulo", "autor", "fecha_publicacion", "cantidad", "isbn", "imagen"]
    success_url = reverse_lazy("listar_libros_cbv")

class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = "inicio/editar_libro.html"
    fields = ["titulo", "autor", "fecha_publicacion", "cantidad", "isbn", "imagen"]
    success_url = reverse_lazy("listar_libros_cbv")

class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "inicio/eliminar_libro.html"
    success_url = reverse_lazy("listar_libros_cbv")
