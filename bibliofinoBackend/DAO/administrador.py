
from bibliofinoBackend.configs.models import Administrador
from bibliofinoBackend.repository.base import BaseRepository
class AdministradorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Administrador)

administrador_repository = AdministradorRepository()

class AdministradorDAO:
    @staticmethod
    def find_all():
        return administrador_repository.find_all()

    @staticmethod
    def create(data):
        return administrador_repository.create(**data)

    @staticmethod
    def find_one(id):
        return administrador_repository.find_one(id)

    @staticmethod
    def find_one_by_user_id(user_id):
        return Administrador.objects.filter(user_id=user_id).first()

    @staticmethod
    def update(data):
        return administrador_repository.update(data.get("id"), **data)

    @staticmethod
    def remove(id):
        return administrador_repository.remove(id)
