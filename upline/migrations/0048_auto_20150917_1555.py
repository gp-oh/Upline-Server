# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0047_media_converted'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address_number',
            field=models.CharField(max_length=255, null=True, verbose_name='address_number', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='address_number',
            field=models.CharField(max_length=255, null=True, verbose_name='address_number', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='level',
            field=models.ForeignKey(editable=False, to='upline.Level', null=True, verbose_name='gradua\xe7\xe3o'),
        ),
    ]
