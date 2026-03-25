from django.contrib import admin
from .models import Jogador
# Register your models here.
@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('numero_camisa', 'nome') 

    fieldsets = (
        ('Informações:', {
            'fields': ('nome','numero_camisa',)
        }),
    )