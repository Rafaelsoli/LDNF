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
    jogadores = models.ManyToManyField('players.Jogador', related_name='time', null=True, blank=True)

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
    

class Jogos(models.Model):
    id = models.UUIDField(primary_key= True, default=uuid.uuid4, editable= False)
    time_casa = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='casa')
    time_visitante = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='visitante')
    gols_casa = models.IntegerField()
    gols_visitante = models.IntegerField()
    data_jogo = models.DateTimeField()

    def __str__(self):
        return f"{self.time_casa.nome} vs {self.time_visitante.nome} - {self.data_jogo.strftime('%Y-%m-%d %H:%M')}"
    
    @property
    def vencedor(self):
        if self.gols_casa > self.gols_visitante:
            return self.time_casa
        elif self.gols_visitante > self.gols_casa:
            return self.time_visitante
        else:
            return None