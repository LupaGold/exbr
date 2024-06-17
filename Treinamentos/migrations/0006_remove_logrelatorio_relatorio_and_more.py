# Generated by Django 5.0.4 on 2024-05-31 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Treinamentos', '0005_alter_logrelatorio_relatorio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logrelatorio',
            name='relatorio',
        ),
        migrations.AddField(
            model_name='logrelatorio',
            name='treinamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Treinamentos.treinamentos', verbose_name='treinamento'),
        ),
    ]