# Generated by Django 5.0.4 on 2024-05-31 02:18

import Treinamentos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Treinamentos', '0002_alter_relatoriosdetreinamento_auxiliar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatoriosdetreinamento',
            name='auxiliar',
            field=models.TextField(blank=True, max_length=50, null=True, validators=[Treinamentos.models.RelatoriosDeTreinamento.Validador_Auxiliar]),
        ),
        migrations.AlterField(
            model_name='relatoriosdetreinamento',
            name='treinador',
            field=models.TextField(blank=True, max_length=50, null=True, validators=[Treinamentos.models.RelatoriosDeTreinamento.Validador_Auxiliar]),
        ),
    ]