# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0038_auto_20150904_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='postal_code',
            field=models.CharField(max_length=255, null=True, verbose_name='postal_code', blank=True),
        ),
    ]
