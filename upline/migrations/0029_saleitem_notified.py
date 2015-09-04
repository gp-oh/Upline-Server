# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0028_auto_20150826_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleitem',
            name='notified',
            field=models.BooleanField(default=False),
        ),
    ]
