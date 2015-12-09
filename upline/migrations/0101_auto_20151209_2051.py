# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0100_auto_20151118_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='invited_members',
            field=models.ManyToManyField(related_name='invited_members', verbose_name='invited members', to='upline.Member', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='invited',
            field=models.ManyToManyField(to='upline.Contact', verbose_name='contatos', blank=True),
        ),
    ]
