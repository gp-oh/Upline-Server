# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import upline.models


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0084_auto_20151009_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(upload_to=upline.models.avatar_path),
        ),
    ]
