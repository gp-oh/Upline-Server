# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('upline', '0101_auto_20151209_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='group',
        ),
        migrations.RemoveField(
            model_name='post',
            name='group',
        ),
        migrations.AddField(
            model_name='event',
            name='groups',
            field=models.ManyToManyField(default=None, to='auth.Group', null=True, verbose_name='grupos', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='groups',
            field=models.ManyToManyField(default=None, to='auth.Group', null=True, verbose_name='grupos', blank=True),
        ),
    ]
