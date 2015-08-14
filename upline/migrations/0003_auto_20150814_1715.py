# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0002_auto_20150814_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='avatar_url',
        ),
        migrations.RemoveField(
            model_name='trainingstep',
            name='media_url',
        ),
        migrations.AddField(
            model_name='member',
            name='avatar',
            field=models.ImageField(null=True, upload_to=b'members', blank=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='media',
            field=models.FileField(null=True, upload_to=b'training_steps', blank=True),
        ),
    ]
