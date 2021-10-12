from django.db import models
# Create your models here.

class Direccion(models.Model):
    
    id = models.AutoField(primary_key = True)
    continente = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    latitud = models.CharField(max_length=50)
    longitud =models.CharField(max_length=50)