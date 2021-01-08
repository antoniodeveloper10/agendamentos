from django.contrib import admin

from pacientes.models import Pacientes
class Paciente(admin.ModelAdmin):
    # informa quais dados iram aparecem no painel de administracao
    list_display = [
        'nome', 
        'data_nasc' ,
        'endereco' ,
        'num_endereco',
        'cep' ,
        'data_cadastro' ,
        'rg'
    ]
    # informa quais campos vao receber links
    list_display_links = ('nome', 'data_nasc')
    # campo de busca
    search_fields = ('nome',)

admin.site.register(Pacientes, Paciente)





