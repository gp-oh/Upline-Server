# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0083_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avatar',
            options={'verbose_name': 'Avatar', 'verbose_name_plural': 'Avatar'},
        ),
        migrations.AddField(
            model_name='post',
            name='converted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='converted',
            field=models.BooleanField(default=False),
        ),
    ]
