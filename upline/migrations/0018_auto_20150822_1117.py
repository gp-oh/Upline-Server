# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0017_auto_20150822_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='reference_value',
        ),
        migrations.RemoveField(
            model_name='saleitem',
            name='delivery_prevision',
        ),
        migrations.AddField(
            model_name='product',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sale',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sale',
            name='send_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]
