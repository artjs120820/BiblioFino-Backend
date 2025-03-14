from django.http import JsonResponse
from bibliofinoBackend.DAO.usuario import UsuarioDAO
from bibliofinoBackend.DAO.ciudadano import CiudadanoDAO

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
