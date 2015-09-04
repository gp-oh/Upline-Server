# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0026_auto_20150826_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='level',
            field=models.ForeignKey(default=1, to='upline.Level'),
            preserve_default=False,
        ),
    ]
