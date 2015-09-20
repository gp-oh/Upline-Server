# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0059_auto_20150919_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='media_type',
            field=models.IntegerField(default=0, verbose_name='tipo de midia', editable=False, choices=[(0, b'Imagem'), (1, b'Audio'), (2, b'Video'), (3, b'Pdf')]),
        ),
    ]
