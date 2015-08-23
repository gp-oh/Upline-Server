# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0020_auto_20150822_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='invited',
        ),
        migrations.AddField(
            model_name='event',
            name='invited',
            field=models.ManyToManyField(to='upline.Contact', null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name='event',
            name='members',
        ),
        migrations.AddField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(to='upline.Member', null=True, blank=True),
        ),
    ]
