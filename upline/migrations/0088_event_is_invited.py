# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0087_auto_20151015_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_invited',
            field=models.BooleanField(default=False),
        ),
    ]
