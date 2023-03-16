from django.db import models

# Create your models here.
class Equipos(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Trabajador(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class ProjectManager(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Proyecto(models.Model):

    nombre = models.CharField(max_length=30)
    fechaentrega = models.DateField()
    entregado = models.BooleanField()

