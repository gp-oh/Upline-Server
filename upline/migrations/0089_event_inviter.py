# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0088_event_is_invited'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='inviter',
            field=models.ForeignKey(related_name='Invited', verbose_name='inviter', blank=True, to='upline.Member', null=True),
        ),
    ]
