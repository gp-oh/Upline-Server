# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0103_auto_20160131_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.IntegerField(default=None, null=True, verbose_name='sexo', blank=True, choices=[(0, b'Masculino'), (1, b'Feminino')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='postal_code',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='CEP', blank=True),
        ),
    ]
