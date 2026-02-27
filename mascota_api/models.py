from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    raza = models.CharField(choices={('Perro', 'perro'), ('Gato', 'gato')}, max_length=20)