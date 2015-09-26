# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0069_auto_20150925_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('upline.contact',),
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-begin_time'], 'verbose_name': 'evento', 'verbose_name_plural': 'eventos'},
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='notificate_at',
            field=models.DateField(default=None, null=True, verbose_name='notificar em', blank=True),
        ),
    ]
