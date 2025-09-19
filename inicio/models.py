from django.db import models




from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    cantidad = models.IntegerField(default=1)
    imagen = models.ImageField(upload_to="libros/", blank=True, null=True)

    def __str__(self):
        return self.titulo
# Create your models here.



# Modelo de Usuario/Socio
class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    grado = models.CharField(max_length=50, blank=True, null=True)  # opcional si es biblioteca escolar/militar
    fecha_alta = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Modelo de Préstamo
class Prestamo(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.socio} - {self.libro}"


# Modelo de Registro de Resultados de Pruebas (si lo incluís en documentación del proyecto)
class RegistroPrueba(models.Model):
    descripcion = models.TextField()
    resultado_esperado = models.TextField()
    resultado_obtenido = models.TextField(blank=True, null=True)
    fecha_prueba = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Prueba: {self.descripcion[:30]}..."