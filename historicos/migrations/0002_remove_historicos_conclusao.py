# Generated by Django 3.1.4 on 2020-12-30 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historicos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicos',
            name='conclusao',
        ),
    ]