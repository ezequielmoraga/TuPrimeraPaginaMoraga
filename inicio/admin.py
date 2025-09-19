from django.contrib import admin
from .models import Libro, Socio, Prestamo, RegistroPrueba

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_publicacion", "cantidad", "isbn")
    search_fields = ("titulo", "autor", "isbn")
    list_filter = ("fecha_publicacion",)

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "grado", "fecha_alta")
    search_fields = ("nombre", "apellido")

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("socio", "libro", "fecha_prestamo", "fecha_devolucion", "devuelto")
    search_fields = ("socio__nombre", "socio__apellido", "libro__titulo")
    list_filter = ("devuelto", "fecha_prestamo")

@admin.register(RegistroPrueba)
class RegistroPruebaAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "resultado_esperado", "resultado_obtenido", "fecha_prueba")
    search_fields = ("descripcion",)
