from django.http import JsonResponse
from bibliofinoBackend.DAO.reserva import ReservaDAO
from bibliofinoBackend.DAO.copia import CopiaDAO
from bibliofinoBackend.DAO.libro import LibroDAO

def obtener_reservas_usuario(request, ciudadano_id):
    """Obtiene todas las reservas de un usuario por su ID de ciudadano, 
    incluyendo la información de las copias y sus libros asociados."""

    reservas = ReservaDAO.find_by_ciudadano_id(ciudadano_id)

    if not reservas.exists():  
        return JsonResponse({"success": False, "message": "No se encontraron reservas para este usuario"})

    reservas_con_detalle = []

    for reserva in reservas:
        copia_id = reserva.copia_id  

        copia = CopiaDAO.find_one(copia_id)
        copia_data = copia.__dict__ if copia else None

        if copia_data and "_state" in copia_data:
            del copia_data["_state"]  

        libro_id = copia.libro_id if copia else None

        libro = LibroDAO.find_one(libro_id) if libro_id else None
        libro_data = libro.__dict__ if libro else None

        if libro_data and "_state" in libro_data:
            del libro_data["_state"]

        reserva_detallada = {
            "reserva_id": reserva.id, 
            "fecha_reserva": reserva.fecha_reserva,
            "fecha_vencimiento": reserva.fecha_vencimiento,
            "estado": reserva.estado,
            "copia": copia_data,
            "libro": libro_data
        }

        reservas_con_detalle.append(reserva_detallada)

    return JsonResponse({"success": True, "reservas": reservas_con_detalle}, safe=False)
