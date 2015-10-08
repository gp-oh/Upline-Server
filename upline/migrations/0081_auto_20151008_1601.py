# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0080_member_outpooring_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='outpooring_level',
            field=models.IntegerField(default=999999, editable=False),
        ),
    ]
