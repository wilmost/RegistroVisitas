from django.db import models

# Create your models here.
class Visitante(models.Model):
    nombre              = models.CharField(max_length = 50)
    apellido            = models.CharField(max_length = 50)
    cedula              = models.CharField(max_length = 11)
    institucion         = models.CharField(max_length = 100)
    posicion            = models.CharField(max_length = 100)
    email               = models.EmailField(max_length = 100)
    direccion           = models.TextField()
    celular             = models.CharField(max_length = 10)
    motivo              = models.TextField()
    hora                = models.TimeField()
   