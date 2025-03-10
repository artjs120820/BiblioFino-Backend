from bibliofinoBackend.configs.models import Token
from bibliofinoBackend.repository.base import BaseRepository


class TokenRepository(BaseRepository):
    def __init__(self):
        super().__init__(Token)

token_repository = TokenRepository()

class TokenDAO:
    @staticmethod
    def find_all():
        return token_repository.find_all()

    @staticmethod
    def create(data):
        return token_repository.create(**data)

    @staticmethod
    def find_one(id):
        return token_repository.find_one(id)

    @staticmethod
    def update(data):
        return token_repository.update(data.get("id"), **data)

    @staticmethod
    def remove(id):
        return token_repository.remove(id)
