from django.db import models
import uuid
from django.urls import reverse


class Time(models.Model):
    #jogadores = models.ForeignKey()
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nome = models.CharField(max_length = 50)
    localidade = models.CharField(max_length = 50)
    descricao = models.TextField()
    escudo = models.URLField(blank = True)

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse("time-detail", args={str(self.id)})
    
    
        
class Placar(models.Model):
    id = models.UUIDField(primary_key= True, default=uuid.uuid4, editable= False)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    jogos = models.IntegerField()
    vitorias = models.IntegerField()
    derrotas = models.IntegerField()
    empate = models.IntegerField()
    GM = models.IntegerField(default=0)
    GS = models.IntegerField(default=0)

    @property
    def pontos(self):
        return (self.vitorias * 3) + (self.empate * 1)
    
    @property
    def DG(self):
        return(self.GM) - (self.GS)
    
    @property
    def PCT(self):
        total_possivel = self.jogos * 3
        return round(self.pontos / total_possivel, 3)