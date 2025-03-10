from django.db import connections

def get_db_connection():
    """Devuelve la conexión a la base de datos configurada en settings.py"""
    return connections['default']
