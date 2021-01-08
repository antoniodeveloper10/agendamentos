from django.contrib import admin

from imagens.models import imagensHistorico

class imagens(admin.ModelAdmin):
    list_display = [
        'id_imagem_historico', 
        'imagens'
    ] 

    list_display_links = ('id_imagem_historico',)
    search_fields = ('id_imagem_historico',)

admin.site.register(imagensHistorico, imagens) 


