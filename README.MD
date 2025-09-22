# Proyecto Final - Biblioteca Virtual (Django)

Este proyecto fue desarrollado como entrega final del curso de Python.  
La aplicación simula una biblioteca virtual, permitiendo gestionar libros, socios y préstamos.  

## Funcionalidades principales

- Inicio: Página principal con navegación hacia todas las secciones.
- CRUD de Libros:
  - Crear, listar, buscar, editar y eliminar libros.
  - Vista de detalle para cada libro.
  - Implementación con funciones (FBV) y clases basadas en vistas (CBV).
- Socios:
  - Registro de socios con nombre, apellido y grado.
  - Listado y búsqueda de socios.
- Préstamos:
  - Registrar préstamos de libros a socios.
  - Listar préstamos activos o devueltos.
- Usuarios:
  - Registro de usuario, inicio y cierre de sesión.
  - Perfil de usuario con datos editables.
  - Cambio de contraseña.
- Vista "Acerca de mí": Información personal del autor del proyecto.

## Tecnologías utilizadas

- Python 3.13
- Django 5.2.6
- SQLite (base de datos)
- HTML, CSS y herencia de templates
- Bootstrap para el diseño
- Pillow (para manejo de imágenes en los modelos)

## Seguridad

- Uso de @login_required en vistas basadas en funciones.
- Uso de LoginRequiredMixin en vistas basadas en clases.
- Redirección automática al login si el usuario no está autenticado.

## Estructura destacada del proyecto

- `inicio/`: App principal (libros, socios, préstamos, acerca de mí).
- `cuentas/`: App de usuarios (login, registro, perfil, cambio de contraseña).
- `templates/`: Carpeta con la base de templates y herencia.
- `static/`: Archivos estáticos (CSS, imágenes del sistema).
- `media/`: Carpeta para subir imágenes (no incluida en GitHub).
- `.gitignore`: Configurado para excluir `db.sqlite3`, `media`, `__pycache__` y el entorno virtual.

## Cómo ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone <url_del_repositorio>

python -m venv venv
venv\Scripts\activate 
pip install -r requirements.txt
7python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
 este seria mi trabajo final se que me falto un monton pero por cuestiones de horaws y de practica es lo que logre termianr espero al devolucion saludos .