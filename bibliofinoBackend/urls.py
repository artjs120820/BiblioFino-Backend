"""
URL configuration for bibliofinoBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bibliofinoBackend.controllers import ciudadano, copia  # ✅ Importamos el módulo en lugar de cada función

urlpatterns = [
    path('admin/', admin.site.urls)
]

# ✅ Agregar más rutas sin sobrecargar urlpatterns
urlpatterns += [
    path('login/', ciudadano.login, name='login'),
    path('buscar_libros/', copia.buscar_libros, name='buscar_libros'),
]