# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0008_auto_20150817_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='quickblox_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
