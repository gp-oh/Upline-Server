# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0043_video_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='quickblox_login',
        ),
        migrations.AlterField(
            model_name='member',
            name='quickblox_id',
            field=models.CharField(verbose_name='id do quickblox', max_length=255, null=True, editable=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='quickblox_password',
            field=models.CharField(verbose_name='senha do quickblox', max_length=255, null=True, editable=False),
        ),
    ]
