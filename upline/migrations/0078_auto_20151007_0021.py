# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0077_auto_20151005_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=255, null=True, verbose_name='email', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='postal_code',
            field=models.CharField(max_length=255, null=True, verbose_name='CEP', blank=True),
        ),
    ]
