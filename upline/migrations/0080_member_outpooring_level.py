# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0079_auto_20151007_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='outpooring_level',
            field=models.IntegerField(default=None, null=True, editable=False, blank=True),
        ),
    ]
