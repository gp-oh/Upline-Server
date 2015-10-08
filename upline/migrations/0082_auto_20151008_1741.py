# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0081_auto_20151008_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Binary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_position', models.IntegerField(default=0)),
                ('can_left', models.BooleanField(default=False)),
                ('can_right', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='member',
            name='outpooring_level',
        ),
        migrations.AddField(
            model_name='binary',
            name='member',
            field=models.ForeignKey(to='upline.Member'),
        ),
        migrations.AddField(
            model_name='binary',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='downlines', verbose_name='pai', blank=True, to='upline.Binary', null=True),
        ),
    ]
