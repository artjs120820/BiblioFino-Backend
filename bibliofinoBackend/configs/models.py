from django.db import models

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