# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0034_auto_20150902_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='outpooring',
            field=models.IntegerField(default=0),
        ),
    ]
