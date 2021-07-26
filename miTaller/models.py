from django.db import models

# Create your models here.
class CategoriaReparacion(models.Model):
    nombreCategoria = models.CharField(primary_key=True,max_length=45)
    numeroCategoria = models.IntegerField()
    def __str__(self):
        return self.nombreCategoria

class Reparacion(models.Model):
    nombreReparacion = models.CharField(primary_key=True,max_length=50)
    codigoReparacion = models.IntegerField()
    descripcionReparacion = models.TextField()
    imagen = models.ImageField(upload_to='taller',null=True)
    publicarReparacion =models.BooleanField(default=False)
    categoriaRep = models.ForeignKey(CategoriaReparacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreReparacion

class Contacto(models.Model):
    nombreContacto = models.CharField(max_length=50)
    apellidoContacto = models.CharField(max_length=50)
    emailContacto = models.CharField(primary_key=True,max_length=50)
    fonoContacto = models.IntegerField()
    mensajeContacto = models.TextField()   

    def __str__(self):
        return self.emailContacto