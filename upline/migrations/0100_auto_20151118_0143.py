# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0099_auto_20151116_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='count_messages_after_finish',
        ),
        migrations.AddField(
            model_name='training',
            name='previous_training',
            field=models.ForeignKey(default=None, blank=True, to='upline.Training', null=True, verbose_name='treinamentos anteriores'),
        ),
        migrations.AlterField(
            model_name='training',
            name='position',
            field=models.IntegerField(default=99999, verbose_name='position'),
        ),
    ]
