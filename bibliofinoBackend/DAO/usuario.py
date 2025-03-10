from bibliofinoBackend.configs.models import Usuario
from bibliofinoBackend.repository.base import BaseRepository


class UsuarioRepository(BaseRepository):
    def __init__(self):
        super().__init__(Usuario)

usuario_repository = UsuarioRepository()

class UsuarioDAO:
    @staticmethod
    def find_all():
        return usuario_repository.find_all()

    @staticmethod
    def create(data):
        return usuario_repository.create(**data)

    @staticmethod
    def find_one(id):
        return usuario_repository.find_one(id)

    @staticmethod
    def update(data):
        return usuario_repository.update(data.get("id"), **data)

    @staticmethod
    def remove(id):
        return usuario_repository.remove(id)
