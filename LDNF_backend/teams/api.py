from datetime import datetime

from teams.models import *
from ninja import Schema, Field
import uuid
from django.shortcuts import get_object_or_404
from typing import List, Optional

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

class TimeSimplesSchema(Schema):
    id: uuid.UUID
    nome: str

class JogoInfoSchema(Schema):
    id: uuid.UUID
    time_casa: TimeSimplesSchema
    time_visitante: TimeSimplesSchema
    gols_casa: int
    gols_visitante: int
    data_jogo: datetime
    vencedor: Optional[TimeSimplesSchema] = None
    

    class Config:
        from_attributes = True

def JogosInfo(api):
    @api.get("/jogos/{time_id}", response=List[JogoInfoSchema])
    def get_jogos(request, time_id: uuid.UUID):
        return Jogos.objects.filter(
        models.Q(time_casa_id=time_id) | models.Q(time_visitante_id=time_id)
        ).select_related('time_casa', 'time_visitante')
    
class JogoCreateSchema(Schema):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    time_casa: uuid.UUID
    time_visitante: uuid.UUID
    gols_casa: int
    gols_visitante: int
    data_jogo: datetime

def JogosCreate(api):
    @api.post("/jogos/create")
    def create_jogo(request, data: JogoCreateSchema):
        jogo = Jogos.objects.create(**data.dict())
        return {"success": True, "jogo_id": jogo.id}