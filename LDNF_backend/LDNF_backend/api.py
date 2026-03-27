from ninja_extra import NinjaExtraAPI
from core.api import *
from ldnf.api import *
from teams.api import *

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

eu(api)
registrar_usuario(api)
SobreLdnf(api)
PlacarInfo(api)
TimeInfo(api)
PlacarUpdate(api)
JogosCreate(api)
JogosInfo(api)