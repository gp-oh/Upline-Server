# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0093_auto_20151025_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='update_media_message',
        ),
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='update_post_message',
        ),
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='update_training_message',
        ),
        migrations.AlterField(
            model_name='media',
            name='media',
            field=s3direct.fields.S3DirectField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='media',
            field=s3direct.fields.S3DirectField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='media_type',
            field=models.IntegerField(default=0, verbose_name='tipo de midia', editable=False, choices=[(0, b'Imagem'), (1, b'Audio'), (2, b'Video'), (3, b'Texto')]),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='media_type',
            field=models.IntegerField(default=0, verbose_name='tipo de midia', editable=False, choices=[(0, b'Imagem'), (1, b'Audio'), (2, b'Video'), (3, b'Texto')]),
        ),
    ]
