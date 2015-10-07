# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0078_auto_20151007_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.IntegerField(default=-1, null=True, verbose_name='sexo', blank=True, choices=[(-1, b'-'), (0, b'Masculino'), (1, b'Feminino')]),
        ),
    ]
