import random
import string
import os
import json

from django.conf import settings
from django.http import JsonResponse
from django.core.mail import send_mail, EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from bibliofinoBackend.DAO.usuario import UsuarioDAO
from bibliofinoBackend.DAO.ciudadano import CiudadanoDAO
from bibliofinoBackend.DAO.codigoVerificacion import CodigoVerificacionDAO
from django.utils.timezone import now
from celery import shared_task

def obtener_usuario_y_ciudadano(request, ciudadano_id):
    """Obtiene los datos del usuario y del ciudadano asociado a un ciudadano_id."""
    
    usuario = UsuarioDAO.find_one_by_id_ciudadano(ciudadano_id)
    if not usuario:
        return JsonResponse({"success": False, "message": "Usuario no encontrado"}, status=404)

    ciudadano = CiudadanoDAO.find_one(ciudadano_id)
    if not ciudadano:
        return JsonResponse({"success": False, "message": "Ciudadano no encontrado"}, status=404)

    usuario_data = usuario.__dict__
    ciudadano_data = ciudadano.__dict__

    for data in (usuario_data, ciudadano_data):
        data.pop("_state", None)

    return JsonResponse({"success": True, "usuario": usuario_data, "ciudadano": ciudadano_data}, safe=False)



def generar_codigo():
    """Genera un código aleatorio de 6 dígitos."""
    return ''.join(random.choices(string.digits, k=6))



def correo_autenticacion(request):
    """Valida si un correo ya está registrado y envía un código si no lo está."""
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "Método no permitido"}, status=405)
    
    try:
        # Leer JSON del request.body
        data = json.loads(request.body.decode("utf-8"))  
        email = data.get("email", "").strip()

        if not email:
            return JsonResponse({"success": False, "message": "El correo es obligatorio"}, status=400)

        usuario = CiudadanoDAO.find_one_by_correo(email)
        if usuario:
            return JsonResponse({"success": False, "message": "El correo ya está registrado"}, status=409)

        # Generar código y guardarlo en la BD
        codigo = generar_codigo()
        CodigoVerificacionDAO.generate_new_code(email, codigo)

        # Verificar si existe el template del correo
        template_path = os.path.join(settings.BASE_DIR, "templates", "codigo_verificacion.html")
        if not os.path.exists(template_path):
            return JsonResponse({"success": False, "message": f"Template no encontrado en {template_path}"}, status=500)

        # Renderizar el mensaje del correo
        html_message = render_to_string("codigo_verificacion.html", {"codigo": codigo})
        plain_message = strip_tags(html_message)  
        
        # Configurar y enviar el correo
        email_message = EmailMessage(
            subject="Tu código de verificación - Bibliofino",
            body=html_message,
            from_email="no-reply@bibliofino.com",  
            to=[email],
        )
        email_message.content_subtype = "html"  
        email_message.extra_headers = {
            "List-Unsubscribe": "<mailto:no-reply@bibliofino.com>",
            "Precedence": "bulk",
        }
        email_message.send(fail_silently=False)

        return JsonResponse({"success": True, "message": "Código enviado correctamente"})

    except json.JSONDecodeError:
        return JsonResponse({"success": False, "message": "Error al decodificar JSON"}, status=400)

    except Exception as e:
        return JsonResponse({"success": False, "message": f"Error interno: {str(e)}"}, status=500)
    
@csrf_exempt
def validar_codigo(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "Método no permitido"}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))  
        email = data.get("email", "").strip()
        codigo_ingresado = data.get("codigo", "").strip()

        if not email or not codigo_ingresado:
            return JsonResponse({"success": False, "message": "Email y código son obligatorios"}, status=400)

        codigo = CodigoVerificacionDAO.find_by_email_and_codigo(email, codigo_ingresado)

        if not codigo:
            return JsonResponse({"success": False, "message": "Código incorrecto o inexistente"}, status=400)

        if codigo.estado != "activo" or codigo.expira_en < now():
            return JsonResponse({"success": False, "message": "Código vencido"}, status=400)

        # Marcar el código como usado (vencido)
        CodigoVerificacionDAO.update(codigo.id, estado="vencido")

        return JsonResponse({"success": True, "message": "Código validado correctamente"})

    except json.JSONDecodeError:
        return JsonResponse({"success": False, "message": "Error al decodificar JSON"}, status=400)

    except Exception as e:
        return JsonResponse({"success": False, "message": f"Error interno: {str(e)}"}, status=500)
    

def crear_usuario(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "Método no permitido"}, status=405)
    
    try:
        data = json.loads(request.body.decode("utf-8"))
        
        dni = data.get("dni", "").strip()
        nombre = data.get("nombre", "").strip()
        apellido = data.get("apellido", "").strip()
        email = data.get("email", "").strip()
        password = data.get("password", "").strip()
        foto_url = data.get("foto_url", "").strip()
        description = data.get("description", "").strip()

        if not all([dni, nombre, apellido, email, password]):
            return JsonResponse({"success": False, "message": "Todos los campos son obligatorios"}, status=400)
        
        # Crear ciudadano
        ciudadano_data = {
            "dni": dni,
            "nombre": nombre,
            "apellido": apellido,
            "correo": email,
            "contrasenia": password,  # En producción, debería ser hasheada
            "email_verificado": 1,
            "distrito_id": 3,
        }
        ciudadano = CiudadanoDAO.create(ciudadano_data)
        
        if not ciudadano:
            return JsonResponse({"success": False, "message": "Error al crear ciudadano"}, status=500)
        
        # Asegúrate de usar el ID del ciudadano
        ciudadano_id = ciudadano.id  # Ahora estamos obteniendo solo el ID
        
        # Crear usuario
        usuario_data = {
            "ciudadano_id": ciudadano_id,
            "foto_url": foto_url,
            "descripcion": description,
            "fecha_registro": now(),
        }
        usuario = UsuarioDAO.create(usuario_data)
        
        if not usuario:
            return JsonResponse({"success": False, "message": "Error al crear usuario"}, status=500)
        
        # Convertir el objeto Usuario a un diccionario
        usuario_dict = {
            "id": usuario.id,
            "ciudadano_id": usuario.ciudadano_id,
            "foto_url": usuario.foto_url,
            "descripcion": usuario.descripcion,
            "fecha_registro": usuario.fecha_registro.isoformat()  # Convertir la fecha a formato ISO
        }
        
        return JsonResponse({"success": True, "message": "Usuario creado exitosamente", "usuario": usuario_dict})

    except json.JSONDecodeError:
        return JsonResponse({"success": False, "message": "Error al decodificar JSON"}, status=400)

    except Exception as e:
        return JsonResponse({"success": False, "message": f"Error interno: {str(e)}"}, status=500)
