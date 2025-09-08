

from django.urls import path
from inicio.views import inicio,crear_libro



urlpatterns = [
    path('vista/', inicio ,name='inicio'),
    path('crear-libro/<titulo>/<autor>/<fecha_publicacion>/', crear_libro,name='crear libro'),
]
