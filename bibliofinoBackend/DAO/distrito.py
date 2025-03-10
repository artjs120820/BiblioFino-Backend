from bibliofinoBackend.configs.models import Distrito
from bibliofinoBackend.repository.base import BaseRepository

class DistritoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Distrito)

distrito_repository = DistritoRepository()

class CistritoDAO:
    @staticmethod
    def find_all():
        return distrito_repository.find_all()

    @staticmethod
    def create(data):
        return distrito_repository.create(**data)

    @staticmethod
    def find_one(id):
        return distrito_repository.find_one(id)

    @staticmethod
    def find_one_by_user_id(user_id):
        return Distrito.objects.filter(user_id=user_id).first()

    @staticmethod
    def update(data):
        return distrito_repository.update(data.get("id"), **data)

    @staticmethod
    def remove(id):
        return distrito_repository.remove(id)
