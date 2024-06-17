# Generated by Django 5.0.4 on 2024-06-16 19:20

import django.db.models.deletion
import django.utils.timezone
import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AjudanteRelatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('palestra', models.CharField(blank=True, max_length=50, null=True, verbose_name=(('Mover (TS) (1)', 'Mover (TS) (1)'), ('Mudança de Patente (TS) (1)', 'Mudança de Patente (TS) (1)'), ('Instalação do TeamSpeak (4)', 'Instalação do TeamSpeak (4)'), ('Instalação de Discord (2)', 'Instalação de Discord (2)'), ('Instalação do Lightshot (2)', 'Instalação do Lightshot (2)'), ('Instalação do Launcher (2)', 'Instalação do Launcher (2)'), ('Cidadania Habbo (3)', 'Cidadania Habbo (3)'), ('Configuração do TeamSpeak (2)', 'Configuração do TeamSpeak (2)'), ('Auxilio com WhatsApp (3)', 'Auxilio com WhatsApp (3)'), ('Ajudar a entrar no QG (1)', 'Ajudar a entrar no QG (1)')))),
                ('patente_treinado', models.CharField(blank=True, choices=[('', 'Selecione a Patente'), ('Cabo', 'Cabo'), ('Aluno', 'Aluno'), ('Terceiro Sargento', 'Terceiro Sargento'), ('Segundo Sargento', 'Segundo Sargento'), ('Primeiro Sargento', 'Primeiro Sargento'), ('Subtenente', 'Subtenente'), ('Cadete', 'Cadete')], max_length=50, null=True)),
                ('treinados', models.TextField(blank=True, default='', max_length=50, null=True)),
                ('treinador_nick', models.TextField(blank=True, max_length=20, null=True)),
                ('solicitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DestaqueAjudantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datatime', models.DateTimeField(default=django.utils.timezone.now)),
                ('militar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='militardestaqueajd', to=settings.AUTH_USER_MODEL)),
                ('solicitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitantedestajd', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuiaAjudantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guia', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Guia')),
                ('datatime', models.DateTimeField(default=django.utils.timezone.now)),
                ('solicitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitanteajd', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]