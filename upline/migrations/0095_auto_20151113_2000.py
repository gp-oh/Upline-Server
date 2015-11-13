# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0094_auto_20151111_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='level',
            options={'ordering': ['points_range_to'], 'verbose_name': 'gradua\xe7\xe3o', 'verbose_name_plural': 'gradua\xe7\xf5es'},
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='first_training_id',
            field=models.ForeignKey(default=None, blank=True, to='upline.TrainingStep', null=True),
        ),
    ]
