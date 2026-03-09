from ninja import NinjaAPI, Schema
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
from .models import Usuario
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ninja import Router
from ninja.security import HttpBearer 

api = NinjaExtraAPI()

api.register_controllers(NinjaJWTDefaultController)



class RegistroSchema(Schema):
    nome: str
    email: str
    senha: str

@api.post("/registrar/")
def registrar_usuario(request, data: RegistroSchema):
    if Usuario.objects.filter(email=data.email).exists():
        # Retorno correto como Dicionário, não como Set
        return 400, {"error": "Este e-mail já está em uso."}
    
    try:
        user = Usuario.objects.criar_usuario(
            nome=data.nome,
            email=data.email,
            senha=data.senha
        )
        return {"success": True, "user_id": str(user.id)}
    except Exception as e:
        return 500, {"error": f"Erro interno: {str(e)}"}