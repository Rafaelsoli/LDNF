from core.models import *
from ninja import Schema
import uuid
class SobreSchema(Schema):
    id: uuid.UUID
    titulo: str

def SobreLdnf(api):
    @api.get("/sobre/", response=SobreSchema)
    def about(request):
        sbr = AboutLDNF.objects.first()
        if not sbr:
            id_vazio = uuid.uuid4()
            return {"id": id_vazio, "titulo": "content"}
        return sbr