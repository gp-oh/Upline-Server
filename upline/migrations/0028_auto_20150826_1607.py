# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0027_auto_20150826_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='level',
            name='gift',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='level',
            name='image',
            field=models.ImageField(null=True, upload_to=b'levels'),
        ),
    ]
