# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0098_sale_external_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='training',
            options={'ordering': ['position'], 'verbose_name': 'treinamento', 'verbose_name_plural': 'treinamentos'},
        ),
        migrations.AddField(
            model_name='training',
            name='position',
            field=models.IntegerField(default=99999),
        ),
    ]
