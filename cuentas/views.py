from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms

# Formulario de edición de perfil
class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

# Registrar usuario
def registrar(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("iniciar_sesion")  # redirige al login
    else:
        form = UserCreationForm()
    return render(request, "cuentas/registrar.html", {"form": form})

# Perfil del usuario
@login_required
def perfil(request):
    return render(request, "cuentas/perfil.html")

# Editar perfil
@login_required
def editar_perfil(request):
    if request.method == "POST":
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("perfil")  # vuelve al perfil
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, "cuentas/editar_perfil.html", {"form": form})
