from bibliofinoBackend.configs.models import CodigoVerificacion
from bibliofinoBackend.repository.base import BaseRepository
from django.utils.timezone import now
from datetime import timedelta

class CodigoVerificacionRepository(BaseRepository):
    def __init__(self):
        super().__init__(CodigoVerificacion)

codigoVerificacion_repository = CodigoVerificacionRepository()

class CodigoVerificacionDAO:
    @staticmethod
    def find_all():
        return codigoVerificacion_repository.find_all()

    @staticmethod
    def create(data):
        return codigoVerificacion_repository.create(**data)

    @staticmethod
    def find_one(id):
        return codigoVerificacion_repository.find_one(id)

    @staticmethod
    def update(id, **data):
        return codigoVerificacion_repository.update(id, **data)


    @staticmethod
    def remove(id):
        return codigoVerificacion_repository.remove(id)

    @staticmethod
    def find_by_email_and_codigo(email, codigo):
        """Busca un código activo asociado a un email."""
        return codigoVerificacion_repository.model.objects.filter(email=email, codigo=codigo, estado="activo").first()


    @staticmethod
    def invalidate_previous_codes(email):
        codigoVerificacion_repository.model.objects.filter(email=email, estado="activo").update(estado="vencido")

    @staticmethod
    def generate_new_code(email, codigo):
        CodigoVerificacionDAO.invalidate_previous_codes(email)  

        nuevo_codigo = CodigoVerificacionDAO.create({
            "email": email,
            "codigo": codigo,
            "estado": "activo",
            "creado_en": now(),
            "expira_en": now() + timedelta(minutes=10) 
        })
        return nuevo_codigo