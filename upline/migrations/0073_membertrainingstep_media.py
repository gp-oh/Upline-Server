# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0072_auto_20150926_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='membertrainingstep',
            name='media',
            field=models.FileField(default=None, null=True, upload_to=b'answer', blank=True),
        ),
    ]
