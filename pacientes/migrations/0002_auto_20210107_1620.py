# Generated by Django 3.1.4 on 2021-01-07 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pacientes',
            options={'managed': True, 'verbose_name': 'paciente', 'verbose_name_plural': 'pacientes'},
        ),
    ]
