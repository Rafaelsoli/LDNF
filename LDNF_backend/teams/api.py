from teams.models import *
from ninja import Schema
import uuid
from typing import List
class TimeSchema(Schema):
    nome: str
    jogos: int
    vitorias: int
    empate: int
    derrotas: int
    pontos: int

def TimeInfo(api):
    @api.get("/time/", response = List[TimeSchema])
    def info(request):
        teams = list(Time.objects.all())
        teams.sort(key=lambda t: (t.pontos, t.vitorias), reverse=True)
        return teams 