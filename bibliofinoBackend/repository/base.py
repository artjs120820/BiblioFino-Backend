from django.db import models

class BaseRepository:
    def __init__(self, model):
        self.model = model

    def find_all(self, **filters):
        try:
            return self.model.objects.filter(**filters)
        except Exception as e:
            print(f"Error al obtener todos los registros: {e}")
            return None

    def create(self, **data):
        try:
            return self.model.objects.create(**data)
        except Exception as e:
            print(f"Error al crear el registro: {e}")
            return None

    def find_one(self, id):
        try:
            return self.model.objects.filter(id=id).first()
        except Exception as e:
            print(f"Error al encontrar el registro: {e}")
            return None

    def update(self, id, **attributes):
        try:
            record = self.model.objects.filter(id=id).first()
            if not record:
                return None
            for key, value in attributes.items():
                setattr(record, key, value)
            record.save()
            return record
        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
            return None

    def remove(self, id):
        try:
            record = self.model.objects.filter(id=id).first()
            if record:
                record.delete()
                return True
            return False
        except Exception as e:
            print(f"Error al eliminar el registro: {e}")
            return None
