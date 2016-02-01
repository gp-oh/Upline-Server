# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0102_auto_20151215_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='membertrainingstep',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 31, 23, 27, 52, 269618), verbose_name='data de cria\xe7\xe3o', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membertrainingstep',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 31, 23, 28, 10, 662035), verbose_name='data de altera\xe7\xe3o', auto_now=True),
            preserve_default=False,
        ),
    ]
