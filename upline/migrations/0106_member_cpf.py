# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0105_auto_20160807_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='cpf',
            field=models.CharField(max_length=20, null=True, verbose_name='CPF', blank=True),
        ),
    ]
