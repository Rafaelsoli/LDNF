from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
from django.db import models

import uuid 
# Create your models here.
class GerenciadorDeUsuarios(UserManager):
    def _criar_usuario(self, nome, email, senha, **campos_extras):
        if not email:
            raise ValueError("email inválido")
        email = self.normalize_email(email)
        usuario = self.model(email=email, nome = nome, **campos_extras)
        usuario.set_password(senha)
        usuario.save(using=self._db)

        return usuario
    
    def criar_usuario(self, nome = None, email = None, senha = None, **campos_extras):
        campos_extras.setdefault('is_staff', False)
        campos_extras.setdefault('is_superuser', False)
        return self._criar_usuario(nome, email, senha, **campos_extras)
    
    def criar_superusuario(self, nome = None, email = None, senha = None, **campos_extras):
        campos_extras.setdefault('is_staff', True)
        campos_extras.setdefault('is_superuser', True)
        return self._criar_usuario(nome, email, senha, **campos_extras)

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    email = models.EmailField(unique = True)
    nome = models.CharField(max_length = 255, blank = True, default = '')
    avatar = models.ImageField(upload_to = 'avatars', blank = True, null = True)

    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)

    ultimo_login = models.DateTimeField(blank = True, null = True)

    objects = GerenciadorDeUsuarios()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []


class Time(models.Model):
    nome = models.CharField(max_length = 50)
    localidade = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 1500)
    #jogadores = models.ForeignKey()
    escudo = models.URLField(blank = True)

class Jogador(models.Model):
    nome = models.CharField(max_length = 30)
    sobrenome = models.CharField(max_length= 30)
    numero_camisa = models.IntegerField()

