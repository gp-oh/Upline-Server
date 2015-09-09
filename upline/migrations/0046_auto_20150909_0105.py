# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0045_member_member_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='audio',
        ),
        migrations.RemoveField(
            model_name='media',
            name='image',
        ),
        migrations.RemoveField(
            model_name='media',
            name='video',
        ),
        migrations.RemoveField(
            model_name='post',
            name='audio',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.RemoveField(
            model_name='trainingstep',
            name='audio',
        ),
        migrations.RemoveField(
            model_name='trainingstep',
            name='image',
        ),
        migrations.RemoveField(
            model_name='trainingstep',
            name='video',
        ),
        migrations.AddField(
            model_name='media',
            name='media',
            field=s3direct.fields.S3DirectField(null=True),
        ),
        migrations.AddField(
            model_name='media',
            name='thumbnail',
            field=models.ImageField(upload_to=b'thumbnails', null=True, verbose_name='thumbnail', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='media',
            field=s3direct.fields.S3DirectField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to=b'thumbnails', null=True, verbose_name='thumbnail', blank=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='media',
            field=s3direct.fields.S3DirectField(null=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='thumbnail',
            field=models.ImageField(upload_to=b'thumbnails', null=True, verbose_name='thumbnail', blank=True),
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
