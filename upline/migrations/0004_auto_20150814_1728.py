# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0003_auto_20150814_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='parent',
            field=models.ForeignKey(related_name='downlines', blank=True, to='upline.Member', null=True),
        ),
    ]
