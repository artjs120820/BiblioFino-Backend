from bibliofinoBackend.configs.models import Libro
from bibliofinoBackend.repository.base import BaseRepository


class LibroRepository(BaseRepository):
    def __init__(self):
        super().__init__(Libro)

libro_repository = LibroRepository()

class LibroDAO:
    @staticmethod
    def find_all():
        return libro_repository.find_all()

    @staticmethod
    def create(data):
        return libro_repository.create(**data)

    @staticmethod
    def find_one(id):
        return libro_repository.find_one(id)

    @staticmethod
    def update(data):
        return libro_repository.update(data.get("id"), **data)

    @staticmethod
    def remove(id):
        return libro_repository.remove(id)
