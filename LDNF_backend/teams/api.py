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
    
class JogadorSchema(Schema):
    nome: str
    numero_camisa: int
class TimeSchema(Schema):
    nome: str
    descricao: str
    localidade: str
    escudo: str = None
    jogadores: List[JogadorSchema] = []
    
    @staticmethod
    def resolve_jogadores(obj):
        return obj.jogadores.all()
    
def TimeInfo(api):
    @api.get("/time/{time_id}", response=TimeSchema)
    def get_time(request, time_id: uuid.UUID): 
        time = get_object_or_404(Time, id=time_id)
        return time


class PlacarUpdateSchema(Schema):
    jogos: int
    vitorias: int
    empate: int
    derrotas: int
    GM: int
    GS: int

def PlacarUpdate(api):
    @api.post("/placar/{time_id}/update")
    def update_placar(request, time_id: uuid.UUID, data: PlacarUpdateSchema):
        # Busca o placar vinculado àquele time específico
        placar = get_object_or_404(Placar, time_id=time_id)
        
        # Atualiza os campos com os dados vindos do Vue
        for attr, value in data.dict().items():
            setattr(placar, attr, value)
        
        placar.save()
        return {"success": True}