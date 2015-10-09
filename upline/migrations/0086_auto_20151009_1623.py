# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import upline.models


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0085_auto_20151009_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='avatar',
            field=models.ImageField(upload_to=upline.models.contacts_path, null=True, verbose_name='avatar', blank=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='image',
            field=models.ImageField(upload_to=upline.models.levels_path, null=True, verbose_name='imagem', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='thumbnail',
            field=models.ImageField(upload_to=upline.models.thumbnails_path, null=True, verbose_name='thumbnail', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(upload_to=upline.models.members_path, null=True, verbose_name='avatar', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='dream1',
            field=models.ImageField(default=None, upload_to=upline.models.dreams_path, null=True, verbose_name='sonho 1', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='dream2',
            field=models.ImageField(default=None, upload_to=upline.models.dreams_path, null=True, verbose_name='sonho 2', blank=True),
        ),
        migrations.AlterField(
            model_name='membertrainingstep',
            name='media',
            field=models.FileField(default=None, null=True, upload_to=upline.models.answer_path, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to=upline.models.thumbnails_path, null=True, verbose_name='thumbnail', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='thumbnail',
            field=models.ImageField(upload_to=upline.models.thumbnails_path, null=True, verbose_name='thumbnail', blank=True),
        ),
    ]
