# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0024_auto_20150822_2146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calendar',
            options={'verbose_name': 'calend\xe1rio', 'verbose_name_plural': 'calend\xe1rios'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'cidade', 'verbose_name_plural': 'cidades'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'contato', 'verbose_name_plural': 'contatos'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'evento', 'verbose_name_plural': 'eventos'},
        ),
        migrations.AlterModelOptions(
            name='goal',
            options={'verbose_name': 'meta', 'verbose_name_plural': 'metas'},
        ),
        migrations.AlterModelOptions(
            name='level',
            options={'verbose_name': 'n\xedvel', 'verbose_name_plural': 'niveis'},
        ),
        migrations.AlterModelOptions(
            name='logmemberlogin',
            options={'verbose_name': 'login de membro', 'verbose_name_plural': 'login de membro'},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'midia', 'verbose_name_plural': 'midia'},
        ),
        migrations.AlterModelOptions(
            name='mediacategory',
            options={'verbose_name': 'categoria de midia', 'verbose_name_plural': 'categorias de midia'},
        ),
        migrations.AlterModelOptions(
            name='mediatype',
            options={'verbose_name': 'tipo de midia', 'verbose_name_plural': 'tipos de midia'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'membro', 'verbose_name_plural': 'membros'},
        ),
        migrations.AlterModelOptions(
            name='membertraingstep',
            options={'verbose_name': 'etapa de treinamento do membro', 'verbose_name_plural': 'etapas de treinamento do membro'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AlterModelOptions(
            name='postalcode',
            options={'verbose_name': 'CEP', 'verbose_name_plural': 'CEPs'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'produto', 'verbose_name_plural': 'produtos'},
        ),
        migrations.AlterModelOptions(
            name='sale',
            options={'verbose_name': 'venda', 'verbose_name_plural': 'vendas'},
        ),
        migrations.AlterModelOptions(
            name='saleitem',
            options={'verbose_name': 'item da venda', 'verbose_name_plural': 'itens da venda'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'estado', 'verbose_name_plural': 'estados'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'time', 'verbose_name_plural': 'times'},
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'verbose_name': 'treinamento', 'verbose_name_plural': 'treinamentos'},
        ),
        migrations.AlterModelOptions(
            name='trainingstep',
            options={'verbose_name': 'etapa de treinamento', 'verbose_name_plural': 'etapas de treinamento'},
        ),
        migrations.RemoveField(
            model_name='media',
            name='media_type',
        ),
        migrations.AlterField(
            model_name='event',
            name='invited',
            field=models.ManyToManyField(to='upline.Contact', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(to='upline.Member', blank=True),
        ),
    ]
