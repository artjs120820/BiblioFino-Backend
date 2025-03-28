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
from bibliofinoBackend.controllers import ciudadano, copia, token, reserva, usuario 

urlpatterns = [
    path('admin/', admin.site.urls)
]

urlpatterns += [
    path('login/', ciudadano.login, name='login'),
    path('buscar_libros/', copia.buscar_libros, name='buscar_libros'),
    path('buscarCiudadanoXToken/', token.buscarCiudadanoXToken, name='buscarCiudadanoXToken'),
    path('logout/', token.logout, name='logout'),
    path('obtener_reservas_usuario/<int:ciudadano_id>/', reserva.obtener_reservas_usuario, name='obtener_reservas_usuario'),
    path('obtener_usuario_y_ciudadano/<int:ciudadano_id>/', usuario.obtener_usuario_y_ciudadano, name='obtener_usuario_y_ciudadano'),
    path('buscarCopiaPorId/<int:id>/', copia.buscarCopiaPorId, name='buscarCopiaPorId'),
    path('correo_autenticacion/', usuario.correo_autenticacion, name='correo_autenticacion'),
    path('validar_codigo/', usuario.validar_codigo, name='validar_codigo'),
    path('verificar_dni/', ciudadano.verificar_dni, name='verificar_dni'),
    path('crear_usuario/', usuario.crear_usuario, name='crear_usuario'),
]