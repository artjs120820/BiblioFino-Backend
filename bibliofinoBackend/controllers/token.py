import json
from django.http import JsonResponse
from bibliofinoBackend.DAO.ciudadano import CiudadanoDAO
from bibliofinoBackend.DAO.token import TokenDAO
from bibliofinoBackend.DAO.administrador import AdministradorDAO

def buscarCiudadanoXToken(request):
    """Busca un ciudadano en la BD a partir de su token."""
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "Método no permitido"}, status=405)
    data = json.loads(request.body)
    token = data.get("token")
    
    if not token:
        return JsonResponse({"success": False, "message": "Token requerido"}, status=400)

    token_obj = TokenDAO.find_by_token(token) 
    if not token_obj:
        return JsonResponse({"success": False, "message": "Token inválido o expirado"}, status=401)

    ciudadano = CiudadanoDAO.find_one(token_obj.ciudadano_id) 
    if not ciudadano:
        return JsonResponse({"success": False, "message": "Ciudadano no encontrado"}, status=404)
    administrador = AdministradorDAO.find_one_by_id_ciudadano(ciudadano.id)
    tipo_usuario = "administrador" if administrador else "usuario"

    ciudadano_data = {
        "id": ciudadano.id,
        "nombre": ciudadano.nombre,
        "correo": ciudadano.correo,
        "tipo_usuario": tipo_usuario
    }

    return JsonResponse({"success": True, "ciudadano": ciudadano_data}, status=200)

def logout(request):
    try:
        data = json.loads(request.body)
        token = data.get("token")

        if not token:
            return JsonResponse({"success": False, "message": "Token no proporcionado"}, status=400)

        token_obj = TokenDAO.find_by_token(token)
        if token_obj:
            token_obj.delete()
            return JsonResponse({"success": True, "message": "Sesión cerrada correctamente"}, status=200)
        else:
            return JsonResponse({"success": False, "message": "Token inválido o ya expirado"}, status=400)

    except json.JSONDecodeError:
        return JsonResponse({"success": False, "message": "Error en el formato del JSON"}, status=400)