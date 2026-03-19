from teams.models import *
from ninja import Schema, Field
import uuid
from django.shortcuts import get_object_or_404
from typing import List

class PlacarSchema(Schema):
    id: uuid.UUID = Field(alias="time.id")
    nome: str = Field(alias="time.nome")
    jogos: int
    vitorias: int
    empate: int
    derrotas: int
    pontos: int
    GM: int
    GS: int
    DG: int
    PCT: float

def PlacarInfo(api):
    @api.get("/placar/", response = List[PlacarSchema])
    def info(request):
        plc = list(Placar.objects.all())
        plc.sort(key=lambda t: (t.pontos, t.vitorias), reverse=True)
        return plc 
    
class TimeSchema(Schema):
    nome: str
    descricao: str
    localidade: str

def TimeInfo(api):
    @api.get("/time/{time_id}", response=TimeSchema)
    def get_time(request, time_id: UUID): 
        time = get_object_or_404(Time, id=time_id)
        return time