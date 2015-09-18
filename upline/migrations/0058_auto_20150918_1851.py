# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0057_auto_20150918_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 18, 18, 51, 16, 363791), verbose_name='data de cria\xe7\xe3o', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 18, 18, 51, 23, 979481), verbose_name='data de altera\xe7\xe3o', auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(help_text='255 characters', max_length=255, verbose_name='mensagem'),
        ),
    ]
