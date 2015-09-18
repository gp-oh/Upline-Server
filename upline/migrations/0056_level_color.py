# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0055_auto_20150918_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='color',
            field=colorful.fields.RGBColorField(default=b'#ffffff'),
        ),
    ]
