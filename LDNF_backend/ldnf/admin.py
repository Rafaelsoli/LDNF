from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# 1. Registro do Usuário Customizado
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Como você não usa 'username' e sim 'email', precisamos ajustar o UserAdmin
    ordering = ('email',)
    list_display = ('email', 'nome', 'is_staff', 'is_active')
    
    # Organiza como os campos aparecem na tela de edição do usuário
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome', 'avatar')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('ultimo_login',)}),
    )
    
    # Campos necessários para criar um usuário via Admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'password'),
        }),
    )
    search_fields = ('email', 'nome')