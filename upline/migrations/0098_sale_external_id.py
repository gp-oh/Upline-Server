# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0097_auto_20151113_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='external_id',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
    ]
