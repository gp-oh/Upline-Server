# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0019_auto_20150822_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='invited',
            field=models.ForeignKey(blank=True, to='upline.Contact', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='members',
            field=models.ForeignKey(blank=True, to='upline.Member', null=True),
        ),
    ]
