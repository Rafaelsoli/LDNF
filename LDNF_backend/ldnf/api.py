from ninja import NinjaAPI, Schema
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
from .models import Usuario
from ninja_jwt.authentication import JWTAuth
from django.contrib.auth.decorators import login_required
from ninja import Router
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from uuid import UUID
api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)


class UserSchema(Schema):
    id: UUID
    nome: str
    email: str
 
@api.get("/eu/", response=UserSchema, auth = JWTAuth())
def eu(request):
    return request.auth

class RegistroSchema(Schema):
    nome: str
    email: str
    senha: str

@api.post("/registrar/")
def registrar_usuario(request, data: RegistroSchema):
    if Usuario.objects.filter(email=data.email).exists():
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