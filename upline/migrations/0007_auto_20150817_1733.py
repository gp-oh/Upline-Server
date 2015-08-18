# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0006_auto_20150817_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='level',
            field=models.ForeignKey(to='upline.Level', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='member',
            name='training_steps',
            field=models.ManyToManyField(to='upline.TrainingStep', null=True),
        ),
    ]
