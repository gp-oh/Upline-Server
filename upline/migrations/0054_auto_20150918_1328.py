# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0053_auto_20150918_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingstep',
            name='media',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
    ]
