import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bibliofinoBackend.DAO.libro import LibroDAO
from bibliofinoBackend.DAO.copia import CopiaDAO

@csrf_exempt
def buscar_libros(request):
    """
    Busca libros por título y devuelve copias relacionadas paginadas de 3 en 3.
    Ejemplo de uso: /buscar_libros/?titulo=romeo%20y%20julieta&page=1
    """
    if request.method != "GET":
        return JsonResponse({"success": False, "message": "Método no permitido"}, status=405)

    try:
        titulo = request.GET.get("titulo", "").strip()
        if not titulo:
            return JsonResponse({"success": False, "message": "El título es obligatorio"}, status=400)
        page = int(request.GET.get("page", 1))
        if page < 1:
            return JsonResponse({"success": False, "message": "Número de página inválido"}, status=400)
        libros = LibroDAO.find_by_titulo(titulo)
        if not libros:
            return JsonResponse({"success": False, "message": "No se encontraron libros"}, status=404)

        copias = []
        for libro in libros:
            copias.extend(CopiaDAO.find_by_libro_id(libro.id)) 

        total_copias = len(copias)
        start = (page - 1) * 3
        end = start + 3
        copias_paginadas = copias[start:end]
        has_next = end < total_copias

        return JsonResponse({
            "success": True,
            "total_copias": total_copias,
            "page": page,
            "has_next": has_next,
            "copias": [{
                "id": c.id,
                "imagen": c.imagen,
                "isbn": c.isbn,
                "libro": {
                    "id": c.libro.id,
                    "titulo": c.libro.titulo,
                    "autor": c.libro.autor,
                    "genero": c.libro.genero
                }
            } for c in copias_paginadas]
        })

    except ValueError:
        return JsonResponse({"success": False, "message": "Número de página inválido"}, status=400)
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)}, status=500)
