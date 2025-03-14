import re
import json
import datetime
import jwt
import time  # ⏳ Necesario para hacer la espera
from django.http import JsonResponse
from django.conf import settings
from bibliofinoBackend.DAO.ciudadano import CiudadanoDAO
from bibliofinoBackend.DAO.administrador import AdministradorDAO
from bibliofinoBackend.DAO.token import TokenDAO

def valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def generate_jwt(payload):
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def generate_unique_token(id, correo, tipo_usuario):   
    while True:
        payload = {
            "id": id,
            "correo": correo,
            "tipo_usuario": tipo_usuario,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=14)
        }
        token = generate_jwt(payload) 
        existing_token = TokenDAO.find_by_token(token) 
        if not existing_token:
            return token 
        time.sleep(1)


def login(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "Método no permitido"}, status=405)

    try:
        data = json.loads(request.body)
        correo = data.get("correo", "").strip()
        contrasenia = data.get("contrasenia", "").strip()

        if not correo or not contrasenia:
            return JsonResponse({"success": False, "message": "Correo y contraseña son obligatorios"}, status=400)

        ciudadano = CiudadanoDAO.find_one_by_correo(correo)
        if not ciudadano or ciudadano.contrasenia != contrasenia:
            return JsonResponse({"success": False, "message": "Credenciales incorrectas"}, status=401)

        administrador = AdministradorDAO.find_one_by_id_ciudadano(ciudadano.id)
        tipo_usuario = "administrador" if administrador else "usuario"
        token = generate_unique_token(ciudadano.id, ciudadano.correo, tipo_usuario)

        fecha_creacion = datetime.datetime.utcnow()
        fecha_expiracion = fecha_creacion + datetime.timedelta(days=14)

        TokenDAO.create({
            "ciudadano_id": ciudadano.id,
            "token": token,
            "fecha_creacion": fecha_creacion,
            "fecha_expiracion": fecha_expiracion
        })

        response = JsonResponse({"success": True, "message": "Inicio de sesión exitoso", "token": token})
        return response

    except Exception as e:
        return JsonResponse({"success": False, "message": f"Error en el servidor: {str(e)}"}, status=500)
