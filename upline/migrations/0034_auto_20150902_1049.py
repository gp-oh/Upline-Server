# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0033_auto_20150902_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='member',
            name='rgt',
        ),
        migrations.AddField(
            model_name='member',
            name='mptt_level',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='lft',
            field=models.PositiveIntegerField(editable=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='downlines', blank=True, to='upline.Member', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='tree_id',
            field=models.PositiveIntegerField(editable=False, db_index=True),
        ),
    ]
