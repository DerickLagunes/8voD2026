from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    paginas = models.IntegerField()
    editorial = models.CharField(max_length=50)