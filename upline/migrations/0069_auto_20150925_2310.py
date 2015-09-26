# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0068_auto_20150925_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='number',
            new_name='address_number',
        ),
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='endere\xe7o', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(max_length=255, null=True, verbose_name='cidade', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='region',
            field=models.CharField(max_length=255, null=True, verbose_name='regi\xe3o', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='state',
            field=models.CharField(max_length=255, null=True, verbose_name='estado', blank=True),
        ),
    ]
