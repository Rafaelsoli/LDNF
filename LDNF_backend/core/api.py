from core.models import *

def SobreLdnf(api):
    @api.get("/test/")
    def about(request):
        return {
            "sobre": "ASDASD"
        }