from django.contrib import admin

from historicos.models import Historicos

class Historico(admin.ModelAdmin):
    list_display = [
        'data',
        'aparecimentos_sintomas',
        'duracao_sintomas',
        'local_dor',
        'tipo_dor',
        'remedios',
        'conclusao'
    ]

    list_display_links = ('data',)
    search_fields = ('data',)

# setar modelos nas URls
admin.site.register(Historicos, Historico) 

# Register your models here.
