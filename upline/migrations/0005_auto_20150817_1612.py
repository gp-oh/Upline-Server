# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
# import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0004_auto_20150814_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='active',
        ),
        migrations.RemoveField(
            model_name='member',
            name='password',
        ),
        migrations.AddField(
            model_name='member',
            name='slug',
            field=models.CharField(max_length=45, null=True, blank=True),
        ),
    ]
