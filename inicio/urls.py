from django.urls import path
from inicio.views import (inicio,crear_libro2,listar_libros,crear_socio,listar_socios,crear_prestamo,listar_prestamos,acerca_de_mi,LibroListView, LibroDetailView, LibroCreateView,
    LibroUpdateView, LibroDeleteView
)


urlpatterns = [
    path("", inicio, name="inicio"),
    path("crear_libro2/", crear_libro2, name="crear_libro2"),
    path("listar_libros/", listar_libros, name="listar_libros"),
    path("crear_socio/", crear_socio, name="crear_socio"),
    path("listar_socios/", listar_socios, name="listar_socios"),
    path("crear_prestamo/", crear_prestamo, name="crear_prestamo"),
    path("listar_prestamos/", listar_prestamos, name="listar_prestamos"),
    path("acerca/", acerca_de_mi, name="acerca"),
    path("libros/", LibroListView.as_view(), name="listar_libros_cbv"),
    path("libros/<int:pk>/", LibroDetailView.as_view(), name="detalle_libro"),
    path("libros/<int:pk>/editar/", LibroUpdateView.as_view(), name="editar_libro"),
    path("libros/<int:pk>/eliminar/", LibroDeleteView.as_view(), name="eliminar_libro"),
]
