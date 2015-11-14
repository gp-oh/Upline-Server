# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0096_auto_20151113_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='siteconfiguration',
            options={'verbose_name': 'Configuration'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='birthday',
            field=models.DateField(default=None, null=True, verbose_name='data de nascimento', blank=True),
        ),
    ]
