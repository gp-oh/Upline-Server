# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0049_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='level',
            field=models.ForeignKey(to='auth.Group'),
        ),
    ]
