# Generated by Django 4.0.6 on 2022-07-20 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0002_endereco_longitude'),
        ('core', '0007_rename_decricao_pontoturistico_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
        ),
    ]
