# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0086_auto_20151009_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='sent',
        ),
        migrations.AddField(
            model_name='sale',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'Novo'), (1, b'Enviado'), (2, b'Aprovado'), (3, b'Cancelado')]),
        ),
    ]
