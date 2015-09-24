# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0066_auto_20150922_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 23, 21, 53, 35, 414147), verbose_name='data de cria\xe7\xe3o', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 23, 21, 53, 40, 965787), verbose_name='data de altera\xe7\xe3o', auto_now=True),
            preserve_default=False,
        ),
    ]
