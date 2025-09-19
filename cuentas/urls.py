from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("iniciar/", auth_views.LoginView.as_view(template_name="cuentas/iniciar_sesion.html"), name="iniciar_sesion"),
    path("salir/", auth_views.LogoutView.as_view(), name="logout"),
    path("registrar/", views.registrar, name="registrar"),
    path("perfil/", views.perfil, name="perfil"),
    path("perfil/editar/", views.editar_perfil, name="editar_perfil"),
]
