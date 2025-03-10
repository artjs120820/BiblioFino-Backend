from django.db import models

class Distrito(models.Model):
    nombre = models.CharField(max_length=255)

class Ciudadano(models.Model):
    dni = models.CharField(max_length=20)  # Longitud del DNI
    nombre = models.CharField(max_length=100)  # Longitud del nombre
    apellido = models.CharField(max_length=100)  # Longitud del apellido
    correo = models.EmailField()
    contrasenia = models.CharField(max_length=255)  # Longitud de la contraseña
    email_verificado = models.BooleanField()
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    class Meta:
        db_table = 'ciudadano'  # Especifica el nombre de la tabla aquí

class Usuario(models.Model):
    ciudadano = models.OneToOneField(Ciudadano, on_delete=models.CASCADE)
    foto_url = models.CharField(max_length=255)  # Longitud para la URL de la foto
    descripcion = models.CharField(max_length=500)  # Longitud para la descripción
    fecha_registro = models.DateTimeField()
    class Meta:
        db_table = 'usuario'  # Especifica el nombre de la tabla aquí

class Administrador(models.Model):
    ciudadano = models.OneToOneField(Ciudadano, on_delete=models.CASCADE)
    class Meta:
        db_table = 'administrador'  # Especifica el nombre de la tabla aquí

class Libro(models.Model):
    titulo = models.CharField(max_length=255)  # Longitud del título
    autor = models.CharField(max_length=255)  # Longitud del autor
    genero = models.CharField(max_length=100)  # Longitud del género
    class Meta:
        db_table = 'libro'  # Especifica el nombre de la tabla aquí    

class Copia(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=20)  # Longitud del ISBN
    idioma = models.CharField(max_length=50)  # Longitud del idioma
    editorial = models.CharField(max_length=255)  # Longitud de la editorial
    anio = models.IntegerField()
    paginas = models.IntegerField()
    imagen = models.TextField()
    codigo_unico = models.CharField(max_length=100)  # Longitud del código único
    disponible = models.BooleanField()
    class Meta:
        db_table = 'copia'  # Especifica el nombre de la tabla aquí


class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    copia = models.ForeignKey(Copia, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField()
    fecha_vencimiento = models.DateTimeField()
    estado = models.CharField(max_length=100)  # Longitud del estado de la reserva
    class Meta:
        db_table = 'reserva'  # Especifica el nombre de la tabla aquí

class Token(models.Model):
    ciudadano = models.ForeignKey(Ciudadano, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)  # Longitud del token
    fecha_creacion = models.DateTimeField()
    fecha_expiracion = models.DateTimeField()
    class Meta:
        db_table = 'token'  # Especifica el nombre de la tabla aquí