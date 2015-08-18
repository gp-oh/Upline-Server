# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0005_auto_20150817_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, editable=False),
        ),
    ]
