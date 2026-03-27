from django.contrib import admin
from .models import Time
from .models import Placar
from .models import Jogos
# Register your models here.
@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id') 

    fieldsets = (
        ('Informações Principais', {
            'fields': ('nome','descricao','localidade',)
        }),
        ('Imagem', {
            'fields': ('escudo',)
        }),
        ('Jogadores', {
            'fields': ('jogadores',)
        }),
    )

@admin.register(Placar)
class PlacarAdmin(admin.ModelAdmin):
    list_display = ('time', 'vitorias', 'id')

    fieldsets = (
        ('Time', {
            'fields': ('time',)
        }),
        ('Placar', {
            'fields': ('jogos','vitorias','derrotas','empate','GM','GS',)
        }),
    )
    
@admin.register(Jogos)
class JogosAdmin(admin.ModelAdmin):
    list_display = ('time_casa', 'time_visitante', 'data_jogo')

    fieldsets = (
        ('Times', {
            'fields': ('time_casa', 'time_visitante')
        }),
        ('Gols', {
            'fields': ('gols_casa', 'gols_visitante')
        }),
        ('Data', {
            'fields': ('data_jogo',)
        }),
    )