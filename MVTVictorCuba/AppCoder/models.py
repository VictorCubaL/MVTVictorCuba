from django.db import models

# Create your models here.

class Familiar(models.Model):

    parentesco = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    fechaNacimiento = models.DateField()