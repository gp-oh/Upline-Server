# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0070_auto_20150926_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='pontuated',
            field=models.BooleanField(default=False, verbose_name='pontuated', editable=False),
        ),
    ]
