from django.db import models

class Fruta(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    sabor = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre
