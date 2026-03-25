import uuid

from django.db import models

class Jogador(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length = 30)
    numero_camisa = models.IntegerField()
    
    def __str__(self):
        return self.nome
    

