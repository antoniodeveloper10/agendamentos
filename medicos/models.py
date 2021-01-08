from django.db import models

# Create your models here.

class Medicos(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'medicos'
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'

    def __str__(self):
        return self.nome