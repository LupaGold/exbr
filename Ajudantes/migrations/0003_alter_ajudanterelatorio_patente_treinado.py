# Generated by Django 5.0.4 on 2024-11-26 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ajudantes', '0002_rename_treinador_nick_ajudanterelatorio_treinador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajudanterelatorio',
            name='patente_treinado',
            field=models.CharField(blank=True, choices=[('', 'Selecione a Patente'), ('Soldado', 'Soldado'), ('Soldado Estrela', 'Soldado Estrela'), ('Cabo', 'Cabo'), ('Aluno', 'Aluno'), ('Terceiro Sargento', 'Terceiro Sargento'), ('Segundo Sargento', 'Segundo Sargento'), ('Primeiro Sargento', 'Primeiro Sargento'), ('Subtenente', 'Subtenente'), ('Cadete', 'Cadete')], max_length=50, null=True),
        ),
    ]