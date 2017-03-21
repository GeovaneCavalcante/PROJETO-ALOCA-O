# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-21 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.DecimalField(decimal_places=3, max_digits=11, verbose_name='CPF')),
                ('rg', models.IntegerField(verbose_name='RG')),
                ('data_hora', models.DateTimeField(auto_now_add=True, verbose_name='Data/Hora')),
                ('cep', models.IntegerField(verbose_name='CEP')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('rua', models.CharField(max_length=50, verbose_name='Rua')),
                ('numero', models.IntegerField(verbose_name='Numero')),
                ('complemento', models.CharField(max_length=70, verbose_name='Complemento')),
            ],
        ),
    ]