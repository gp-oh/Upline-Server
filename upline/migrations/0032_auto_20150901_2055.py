# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0031_member_mptt_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='member',
            name='mptt_level',
        ),
        migrations.RemoveField(
            model_name='member',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='member',
            name='tree_id',
        ),
        migrations.AlterField(
            model_name='member',
            name='parent',
            field=models.ForeignKey(related_name='downlines', blank=True, to='upline.Member', null=True),
        ),
    ]
