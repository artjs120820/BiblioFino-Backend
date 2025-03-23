from django.db import models
from django.utils.timezone import now
from datetime import timedelta

class Distrito(models.Model):
    nombre = models.CharField(max_length=255)

class Ciudadano(models.Model):
    dni = models.CharField(max_length=20) 
    nombre = models.CharField(max_length=100) 
    apellido = models.CharField(max_length=100)  
    correo = models.EmailField()
    contrasenia = models.CharField(max_length=255)  
    email_verificado = models.BooleanField()
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    class Meta:
        db_table = 'ciudadano'  

class Usuario(models.Model):
    ciudadano = models.OneToOneField(Ciudadano, on_delete=models.CASCADE)
    foto_url = models.CharField(max_length=255) 
    descripcion = models.CharField(max_length=500) 
    fecha_registro = models.DateTimeField()
    class Meta:
        db_table = 'usuario' 

class Administrador(models.Model):
    ciudadano = models.OneToOneField(Ciudadano, on_delete=models.CASCADE)
    class Meta:
        db_table = 'administrador' 

class Libro(models.Model):
    titulo = models.CharField(max_length=255) 
    autor = models.CharField(max_length=255) 
    genero = models.CharField(max_length=100) 
    class Meta:
        db_table = 'libro' 

class Copia(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=20) 
    idioma = models.CharField(max_length=50) 
    editorial = models.CharField(max_length=255) 
    anio = models.IntegerField()
    paginas = models.IntegerField()
    imagen = models.TextField()
    codigo_unico = models.CharField(max_length=100)  
    disponible = models.BooleanField()
    class Meta:
        db_table = 'copia' 


class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    copia = models.ForeignKey(Copia, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField()
    fecha_vencimiento = models.DateTimeField()
    estado = models.CharField(max_length=100)  
    class Meta:
        db_table = 'reserva' 

class Token(models.Model):
    ciudadano = models.ForeignKey(Ciudadano, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)  
    fecha_creacion = models.DateTimeField()
    fecha_expiracion = models.DateTimeField()
    class Meta:
        db_table = 'token' 



class CodigoVerificacion(models.Model):
    email = models.EmailField() 
    codigo = models.CharField(max_length=6)  
    creado_en = models.DateTimeField(auto_now_add=True)  
    expira_en = models.DateTimeField(default=lambda: now() + timedelta(minutes=10)) 
    estado = models.CharField(max_length=10, choices=[('activo', 'Activo'), ('vencido', 'Vencido')], default='activo')  

    class Meta:
        db_table = 'codigo_verificacion'

    def marcar_vencido(self):
        """Marca este código como vencido."""
        self.estado = 'vencido'
        self.save()

    @staticmethod
    def invalidar_codigos_anteriores(email):
        """Vence cualquier código activo previo para un email."""
        CodigoVerificacion.objects.filter(email=email, estado='activo').update(estado='vencido')

    def es_valido(self):
        """Verifica si el código sigue activo y no ha expirado."""
        return self.estado == 'activo' and self.expira_en > now()