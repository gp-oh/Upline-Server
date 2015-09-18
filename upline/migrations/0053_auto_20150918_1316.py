# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0052_auto_20150918_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingstep',
            name='have_notifications',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='thumbnail',
            field=models.ImageField(verbose_name='thumbnail', upload_to=b'thumbnails', null=True, editable=False, blank=True),
        ),
    ]
