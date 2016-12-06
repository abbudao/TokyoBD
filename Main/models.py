from django.db import models

# Create your models here.
class HabilitadoArbitrar(models.Model):

    def __str__(self):
        return self.codigo

    codigo = models.IntegerField() 
    esporte= models.CharField(max_length=30)

