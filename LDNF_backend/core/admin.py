from django.contrib import admin
from .models import AboutLDNF

# Register your models here.
@admin.register(AboutLDNF)
class SobreAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo') 

    fieldsets = (
        ('Informações Principais', {
            'fields': ('titulo',)
        }),
    )