# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0032_auto_20150901_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='depth',
            field=models.PositiveIntegerField(default=0, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='lft',
            field=models.PositiveIntegerField(default=0, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='rgt',
            field=models.PositiveIntegerField(default=0, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='tree_id',
            field=models.PositiveIntegerField(default=0, db_index=True),
            preserve_default=False,
        ),
    ]
