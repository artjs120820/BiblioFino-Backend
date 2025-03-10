import re
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bibliofinoBackend.DAO.ciudadano import CiudadanoDAO

def valid_email(email):
    """Valida el formato del correo electrónico."""
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

@csrf_exempt
def login(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "Método no permitido"}, status=405)

    try:
        data = json.loads(request.body)
        correo = data.get("correo", "").strip()  # Cambié 'email' por 'correo'
        contrasenia = data.get("contrasenia", "").strip()  # Cambié 'password' por 'contrasenia'

        if not correo or not contrasenia:
            return JsonResponse({"success": False, "message": "Correo y contraseña son obligatorios"}, status=400)

        if not valid_email(correo):
            return JsonResponse({"success": False, "message": "Formato de correo inválido"}, status=400)

        ciudadano = CiudadanoDAO.find_one_by_correo(correo)  # Cambié la función para buscar por 'correo'
        if not ciudadano or ciudadano.contrasenia != contrasenia:  # Cambié 'password' por 'contrasenia'
            return JsonResponse({"success": False, "message": "Credenciales incorrectas"}, status=401)

        return JsonResponse({"success": True, "message": "Inicio de sesión exitoso", "ciudadano": ciudadano.nombre})

    except json.JSONDecodeError:
        return JsonResponse({"success": False, "message": "Formato JSON inválido"}, status=400)

