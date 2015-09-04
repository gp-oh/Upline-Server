# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0025_auto_20150826_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediacategory',
            name='media_type',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='MediaType',
        ),
    ]
