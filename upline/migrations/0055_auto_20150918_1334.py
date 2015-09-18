# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0054_auto_20150918_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingstep',
            name='meetings_per_week',
            field=models.IntegerField(null=True, verbose_name='reuni\xf5es por semana', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='nr_contacts',
            field=models.IntegerField(null=True, verbose_name='n\xfamero de contatos', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='weeks',
            field=models.IntegerField(null=True, verbose_name='semanas', blank=True),
        ),
    ]
