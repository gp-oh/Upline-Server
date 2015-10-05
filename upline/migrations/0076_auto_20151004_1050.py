# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0075_auto_20150926_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='data de altera\xe7\xe3o')),
                ('member', models.ForeignKey(to='upline.Member')),
            ],
            options={
                'verbose_name': 'Invite',
                'verbose_name_plural': 'Invites',
            },
        ),
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ['-create_time'], 'verbose_name': 'venda', 'verbose_name_plural': 'vendas'},
        ),
        migrations.AlterModelOptions(
            name='trainingstep',
            options={'ordering': ['step'], 'verbose_name': 'etapa de treinamento', 'verbose_name_plural': 'etapas de treinamento'},
        ),
    ]
