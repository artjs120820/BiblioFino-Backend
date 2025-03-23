
from bibliofinoBackend.configs.models import Ciudadano
from bibliofinoBackend.repository.base import BaseRepository


class CiudadanoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Ciudadano)

ciudadano_repository = CiudadanoRepository()

class CiudadanoDAO:
    @staticmethod
    def find_all():
        return ciudadano_repository.find_all()

    @staticmethod
    def create(data):
        return ciudadano_repository.create(**data)

    @staticmethod
    def find_one(id):
        return ciudadano_repository.find_one(id)

    @staticmethod
    def find_one_by_user_id(user_id):
        return Ciudadano.objects.filter(user_id=user_id).first()

    @staticmethod
    def update(data):
        return ciudadano_repository.update(data.get("id"), **data)

    @staticmethod
    def remove(id):
        return ciudadano_repository.remove(id)
    
    @staticmethod
    def find_one_by_correo(correo):
        return Ciudadano.objects.filter(correo=correo).first()
    @staticmethod
    def find_one_by_dni(dni):  # ✅ Nuevo método para buscar por DNI
        return Ciudadano.objects.filter(dni=dni).first()