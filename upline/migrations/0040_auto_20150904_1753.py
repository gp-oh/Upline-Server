# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0039_auto_20150904_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.CharField(max_length=255, null=True, verbose_name='status', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='answer_type',
            field=models.IntegerField(verbose_name='tipo de resposta', choices=[(0, 'text'), (1, 'audio'), (2, 'video'), (3, 'list'), (4, 'meeting')]),
        ),
    ]
