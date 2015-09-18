# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0051_auto_20150918_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='count_messages_after_finish',
            field=models.ForeignKey(verbose_name='previous training', to='upline.Training', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='have_notifications',
            field=models.BooleanField(default=False),
        ),
    ]
