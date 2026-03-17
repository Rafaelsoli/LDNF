from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from LDNF_backend.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
