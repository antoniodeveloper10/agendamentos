from django.db import models
from agendamentos.models import Agendamentos


class Historicos(models.Model):
    id_historico = models.AutoField(primary_key=True)
    data = models.DateTimeField(auto_now_add=True)
    aparecimentos_sintomas = models.CharField(max_length=100, blank=True, null=True)
    duracao_sintomas = models.CharField(max_length=100, blank=True, null=True)
    local_dor = models.CharField(max_length=100, blank=True, null=True)
    tipo_dor = models.CharField(max_length=100, blank=True, null=True)
    remedios = models.CharField(max_length=100, blank=True, null=True)
    conclusao = models.CharField(max_length=100, blank=True, null=True)
    id_agendamento = models.ForeignKey(Agendamentos, on_delete=models.CASCADE, related_name='historicos', blank=False, null=False )

    


    class Meta:
        managed = True
        db_table = 'historicos'
        verbose_name = 'historico'
        verbose_name_plural = 'historicos'

 
    

