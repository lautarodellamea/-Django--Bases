"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Define la ruta base del proyecto, que se usa para construir otras rutas dentro del mismo.
BASE_DIR = Path(__file__).resolve().parent.parent


# Django lo usa para mejorar la encriptacion de los usuarios o para generar datos que pueden compartir el navegador con el servidor
# Clave secreta que Django usa para asegurar datos sensibles, como contraseñas y cookies de sesión. Debe mantenerse en secreto en producción.
SECRET_KEY = 'django-insecure--r2+e(bt#2(=my6jbnqq5j1egy%!eaku_*ut_)4fh04j96q@m2'

# Activa el modo de depuración, que muestra errores detallados. Debe estar en False en producción para evitar exponer información sensible.
DEBUG = True
# DEBUG = False


# Lista de dominios/nombres de host que pueden acceder a la aplicación. Es importante configurarlo en producción para evitar accesos no autorizados.
ALLOWED_HOSTS = []


# Lista de aplicaciones habilitadas en el proyecto. Incluye las aplicaciones de Django por defecto y otras que añadas.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # agregamos nuestras aplicaciones, para que detecte migraciones y demas cosas
    'myapp',
]

# Lista de middleware que procesan las peticiones y respuestas, añadiendo funcionalidades como seguridad, sesiones, y autenticación.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Ruta del archivo que contiene las configuraciones de URLs del proyecto (por defecto, mysite.urls).
ROOT_URLCONF = 'mysite.urls'


# Configuración para el sistema de plantillas de Django, incluyendo opciones como directorios de plantillas y procesadores de contexto.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Punto de entrada para que los servidores web compatibles con WSGI puedan servir tu aplicación. Se refiere al archivo wsgi.py del proyecto.
# Cuando despliegas una aplicación Django en producción, el servidor web necesita una forma estándar de interactuar con tu aplicación. WSGI (Web Server Gateway Interface) es ese estándar. La variable WSGI_APPLICATION señala a Django dónde encontrar el archivo que expone la aplicación como un objeto WSGI. En este caso, apunta a mysite.wsgi.application, que es el módulo y la aplicación WSGI en tu proyecto.
WSGI_APPLICATION = 'mysite.wsgi.application'


# https://docs.djangoproject.com/en/5.1/ref/databases/#postgresql-notes
# Configuración de la base de datos. Aquí se especifica el motor de la base de datos (por ejemplo, SQLite) y la ruta donde se almacenará.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validadores de contraseñas que aseguran que las contraseñas de los usuarios cumplan con ciertos criterios de seguridad.o
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Código del idioma predeterminado para el proyecto.
LANGUAGE_CODE = 'en-us'

# Zona horaria predeterminada del proyecto.
TIME_ZONE = 'UTC'

# Habilita la internacionalización, permitiendo que la aplicación soporte múltiples idiomas.
USE_I18N = True

# Habilita el soporte para zonas horarias en la base de datos.
USE_TZ = True

# https://docs.djangoproject.com/en/5.1/howto/static-files/
# URL donde se sirven los archivos estáticos (CSS, JavaScript, imágenes).
STATIC_URL = 'static/'

# Tipo de campo de clave primaria por defecto para modelos en Django.
# En Django, cada modelo necesita una clave primaria (un identificador único para cada registro en la base de datos). Por defecto, Django crea un campo id automáticamente si no defines una clave primaria explícita. DEFAULT_AUTO_FIELD especifica qué tipo de campo será ese id. En este caso, BigAutoField es un campo de tipo entero con un rango mayor que AutoField, lo que permite manejar más registros en la base de datos sin riesgo de que el contador se quede sin valores.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# los archivos asgi.py y wsgi.py son modulos que nos sirven para servir mi contenido a la hora de desplegarlo, ya que Django solo nos permite crear aplicaciones, este no se ocupa de servir contenido en produccion.
