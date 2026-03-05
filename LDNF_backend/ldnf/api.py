from ninja import NinjaAPI, Schema
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
from .models import Usuario
api = NinjaExtraAPI()

api.register_controllers(NinjaJWTDefaultController)

class RegistroSchema(Schema):
    nome: str
    email: str
    senha: str

@api.post("/registrar")
def registrar_usuario(request, data: RegistroSchema):
    if Usuario.objects.filter(email=data.email).exists():
        return {"erro: Esse email já está em uso"}, 400
    
    user = Usuario.objects.criar_usuario(
        nome = data.nome,
        email = data.email,
        senha = data.senha
    )

    return {"Success": True, "user_id": str(user.id)}