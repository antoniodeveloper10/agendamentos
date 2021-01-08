from django.contrib import admin
from agendamentos.models import Agendamentos

class agendamento(admin.ModelAdmin):
    list_display = [
        'id_agendamento', 
        'data_hora' ,
        'data_criacao' ,
        'cancelado',
        'obs' ,
        'tipo'
    ]
    # informa quais campos vao receber links
    list_display_links = ('id_agendamento',)
    # campo de busca
    search_fields = ('id_agendamento',)

# setar modelos nas URls
admin.site.register(Agendamentos, agendamento) 