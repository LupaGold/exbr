# Generated by Django 5.0.4 on 2024-08-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recrutamento', '0005_alter_re_abertura_alter_re_fechamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='re',
            name='militar',
            field=models.CharField(default=' ', max_length=250, null=True),
        ),
    ]