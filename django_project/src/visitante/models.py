from django.db import models
from django.utils import timezone

# Create your models here.



class Instituciones(models.Model):
    nombre              =models.CharField(max_length = 100)
    tipo                =models.CharField(max_length=50)
    autorizador         =models.CharField(max_length = 100)
    email_autorizador   =models.EmailField(max_length = 100)
    Tel_autorizador     =models.CharField(max_length = 10) 

    def __str__(self):
        return self.nombre 


class Visitante(models.Model):
    nombre              = models.CharField(max_length = 50)
    apellido            = models.CharField(max_length = 50)
    cedula              = models.CharField(max_length = 11)
    institucion         = models.ForeignKey(Instituciones,  on_delete=models.CASCADE )
    posicion            = models.CharField(max_length = 100)
    email               = models.EmailField(max_length = 100)
    direccion           = models.TextField()
    celular             = models.CharField(max_length = 10)
    motivo              = models.TextField()
    hora                = models.TimeField()
    fecha               = models.DateTimeField(default=timezone.now)
    entrada             = models.TimeField(blank=True,  null=True)
    salida              = models.TimeField(blank=True,  null=True) 
    duracion            = models.CharField(blank=True, max_length = 10)


    
