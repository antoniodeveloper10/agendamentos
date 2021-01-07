from django.db import models
from historicos.models import Historicos

# Create your models here.

def imagens_historicos(instance, filename):
    return '/'.join(['historicos',str(instance.id_historico.id_historico),filename])

class imagensHistorico(models.Model):
    id_imagem_historico = models.AutoField(primary_key=True)    
    imagens = models.ImageField(upload_to=imagens_historicos, blank=True, null=True)
    id_historico = models.ForeignKey(Historicos, related_name='imagens', on_delete=models.CASCADE, blank=False, null=False)

