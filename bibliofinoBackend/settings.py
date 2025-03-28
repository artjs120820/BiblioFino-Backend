"""
Django settings for bibliofinoBackend project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import glob

# Usar glob para encontrar todas las carpetas de aplicaciones dentro de bibliofinoBackend
app_dirs = glob.glob(os.path.join(os.path.dirname(__file__), 'bibliofinoBackend', '*'))

# Filtrar las aplicaciones que son directorios (y no archivos)
apps = [os.path.basename(app_dir) for app_dir in app_dirs if os.path.isdir(app_dir)]
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6u)^qq&*x=8+d+qv=t59wtx0qc1y$)6epth3i9k!270!ovs%1z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




# Configurar sesiones en base de datos
SESSION_ENGINE = "django.contrib.sessions.backends.db"

# Habilitar HttpOnly para seguridad
SESSION_COOKIE_HTTPONLY = True  

SESSION_COOKIE_SECURE = False  

SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  

SESSION_COOKIE_SAMESITE = "None"

CSRF_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SECURE = False  


AUTH_COOKIE_NAME = "auth_token"  
AUTH_COOKIE_HTTPONLY = True  
AUTH_COOKIE_SECURE = False 
AUTH_COOKIE_SAMESITE = "Lax"  
AUTH_COOKIE_MAX_AGE = 86400  

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bibliofinoBackend.configs', 
    'corsheaders',

]

INSTALLED_APPS += [f'bibliofinoBackend.{app}' for app in apps]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


CORS_ALLOW_CREDENTIALS = True  
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", 
]





ROOT_URLCONF = 'bibliofinoBackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Busca dentro de bibliofinoBackend/templates
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


WSGI_APPLICATION = 'bibliofinoBackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbbibliofino', #CAMBIAR
        'USER': 'arturo', #CAMBIAR
        'PASSWORD': 'kekito120820', #CAMBIAR
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





# EMAILLLL
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "bibliofino.noreply@gmail.com"  # Reemplaza con tu correo
EMAIL_HOST_PASSWORD = "elcb eaom lqby desa"  # O una contraseña de aplicación si tienes 2FA