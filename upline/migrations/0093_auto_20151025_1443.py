# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0092_auto_20151025_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='siteconfiguration',
            options={'verbose_name': 'Mensagens de notifica\xe7\xe3o'},
        ),
        migrations.AddField(
            model_name='media',
            name='notified',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='post',
            name='notified',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='training',
            name='notified',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
