# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0062_auto_20150920_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
    ]
