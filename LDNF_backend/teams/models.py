from django.db import models
import uuid
# Create your models here.
class Time(models.Model):
    #jogadores = models.ForeignKey()
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nome = models.CharField(max_length = 50)
    localidade = models.CharField(max_length = 50)
    descricao = models.TextField()
    escudo = models.URLField(blank = True)
    jogos = models.IntegerField()
    vitorias = models.IntegerField()
    derrotas = models.IntegerField()
    empate = models.IntegerField()
