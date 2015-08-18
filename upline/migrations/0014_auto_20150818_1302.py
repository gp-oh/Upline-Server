# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0013_auto_20150818_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='quickblox_id',
            new_name='quickblox_login',
        ),
        migrations.AddField(
            model_name='member',
            name='quickblox_password',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
