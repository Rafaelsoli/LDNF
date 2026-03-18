from django.contrib import admin
from .models import Time
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
        ('Jogos', {
            'fields': ('jogos','vitorias','derrotas','empate',)
        }),
    )