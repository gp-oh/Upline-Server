# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0065_auto_20150922_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediacategory',
            name='media_type',
        ),
        migrations.AddField(
            model_name='media',
            name='media_type',
            field=models.IntegerField(default=0, verbose_name='tipo de midia', editable=False, choices=[(0, b'Imagem'), (1, b'Audio'), (2, b'Video'), (3, b'PDF')]),
        ),
    ]
