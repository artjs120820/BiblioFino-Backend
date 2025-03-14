from bibliofinoBackend.configs.models import Reserva
from bibliofinoBackend.repository.base import BaseRepository

class ReservaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Reserva)

reserva_repository = ReservaRepository()

class ReservaDAO:
    @staticmethod
    def find_all():
        return reserva_repository.find_all()

    @staticmethod
    def create(data):
        return reserva_repository.create(**data)

    @staticmethod
    def find_one(id):
        return reserva_repository.find_one(id)

    @staticmethod
    def update(data):
        return reserva_repository.update(data.get("id"), **data)

    @staticmethod
    def remove(id):
        return reserva_repository.remove(id)
    
    @staticmethod
    def find_by_ciudadano_id(ciudadano_id):
        return Reserva.objects.filter(usuario_id=ciudadano_id)