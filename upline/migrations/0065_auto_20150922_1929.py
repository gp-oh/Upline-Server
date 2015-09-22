# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0064_member_member_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingstep',
            name='answer_type',
            field=models.IntegerField(default=None, null=True, verbose_name='tipo de resposta', choices=[(0, 'texto'), (1, '\xe1udio'), (2, 'video'), (5, 'imagem'), (3, 'lista'), (4, 'reuni\xe3o')]),
        ),
    ]
