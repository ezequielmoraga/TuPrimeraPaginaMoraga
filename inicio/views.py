


from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Libro


# Create your views here.
def inicio (request):
    return render(request,'inicio/inicio.html')

def crear_libro (request,nombre,autor,fecha_publicacion):
    
    libro=Libro(nombre=nombre,autor=autor,fecha_publicacion=fecha_publicacion)
    libro.save()
    
    return render(request,'inicio/crear_libro.html')