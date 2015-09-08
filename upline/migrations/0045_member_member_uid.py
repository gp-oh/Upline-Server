# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0044_auto_20150908_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_uid',
            field=models.UUIDField(null=True, unique=True, editable=False),
        ),
    ]
