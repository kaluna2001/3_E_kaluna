from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=65, null=False)
    correo = models.CharField(max_length=70, null=False)
    contrasena = models.CharField(max_length=15, null=False)
    estado = models.BooleanField(null=False)
    class Meta:
        db_table = 'usuarios'

class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=25, null=False)
    documento = models.CharField(max_length=10, null=False)
    nombres = models.CharField(max_length=25, null=False)
    apellidos = models.CharField(max_length=25, null=False)
    genero = models.CharField(max_length=7, null=False)
    fecha_nacimiento = models.DateField(null=False)
    telefono = models.CharField(max_length=10, null=False)
    correo = models.CharField(max_length=70, null=False)
    direccion = models.CharField(max_length=100, null=False)
    estado = models.BooleanField(null=False)
    class Meta:
        db_table = 'clientes'

class Mascotas(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, null=True, blank=False, on_delete=models.CASCADE)
    tipo_mascota = models.CharField(max_length=6, null=False)
    nombre = models.CharField(max_length=35, null=False)
    sexo = models.CharField(max_length=7, null=False)
    fecha_nacimiento = models.DateField(null=False)
    raza = models.CharField(max_length=25, null=False)
    estado = models.BooleanField(null=False)
    class Meta:
        db_table = 'mascotas'

class Agendar_Cita(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, null=True, blank=False, on_delete=models.CASCADE)
    id_mascota = models.ForeignKey(Mascotas, null=True, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField(null=False)
    hora = models.TimeField(null=False)
    estado = models.BooleanField(null=False)
    class Meta:
        db_table = 'agendar_cita'