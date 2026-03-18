from django.db import models

# Create your models here.

class Jogador(models.Model):
    nome = models.CharField(max_length = 30)
    sobrenome = models.CharField(max_length= 30)
    numero_camisa = models.IntegerField()

