from bibliofinoBackend.configs.models import Copia
from bibliofinoBackend.repository.base import BaseRepository

class CopiaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Copia)

copia_repository = CopiaRepository()

class CopiaDAO:
    @staticmethod
    def find_all():
        return copia_repository.find_all()

    @staticmethod
    def create(data):
        return copia_repository.create(**data)

    @staticmethod
    def find_one(id):
        return copia_repository.find_one(id)

    @staticmethod
    def find_one_by_user_id(user_id):
        return Copia.objects.filter(user_id=user_id).first()

    @staticmethod
    def update(data):
        return copia_repository.update(data.get("id"), **data)

    @staticmethod
    def remove(id):
        return copia_repository.remove(id)
    @staticmethod
    def find_by_libro_id(libro_id):
        """
        Encuentra todas las copias asociadas a un libro específico.
        """
        return Copia.objects.filter(libro_id=libro_id)

    @staticmethod
    def update(data):
        return copia_repository.update(data.get("id"), **data)