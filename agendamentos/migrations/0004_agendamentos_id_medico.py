# Generated by Django 3.1.4 on 2021-01-07 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0001_initial'),
        ('agendamentos', '0003_auto_20210107_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamentos',
            name='id_medico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='agendamentosMedicos', to='medicos.medicos'),
            preserve_default=False,
        ),
    ]
