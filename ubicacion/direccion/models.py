from django.db import models
# Create your models here.

class Direccion(models.Model):
    
    """
    Modelo de ubicacion con algunas feature properties de pelias, modelo de ubicacion aplicado para obtener la ubicacion de terceros,
    permite crear una ubicacion para un tercer o asignarle una direccion a un tercero  mediante el formato json de pelias.

    Atributos:
        id (int): Identificador unico de una ubicacion
        continente (str): Identificador de un continente existente o disponible
        pais (str): Identificador de un pais anexo para argo diseño
        region (str): Identificador de una region asociada aun pais existente
        ciudad (str): Identificador de una ciudad de un pais existente
        direccion (str): Identificador de ubicacion precisa de un tercero asociado
        latitud (str): Identificador de latitud en standar global
        longitud (str): Identificador de longitud en estandar global
    """

    id = models.AutoField(primary_key = True)
    continente = models.CharField(max_length=20)
    pais = models.CharField(max_length=30)
    region = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    latitud = models.CharField(max_length=50)
    longitud =models.CharField(max_length=50)



    """ 
    #faltarian los coments
    Class Continentes(models.Model):

        id = models.AutoField(primary_key = True)
        nombre_continente = models.CharField(max_length=10)

        def __str__(self):
            return self.nombre_continente


    Class Paises(models.Model):

        id = models.AutoField(primary_key = True)
        pais = models.CharField(max_length=30)

        def __str__(self):
            return self.pais
    

    Class Regiones(models.Model):

        id = models.AutoField(primary_key = True)
        region = models.CharField(max_length=40)

        def __str__(self):
            return self.region
    

    Class Ciudades(models.Model):

        id = models.AutoField(primary_key = True)
        ciudades = models.CharField(max_length=40)

        def __str__(self):
            return self.ciudades
    
    
     """