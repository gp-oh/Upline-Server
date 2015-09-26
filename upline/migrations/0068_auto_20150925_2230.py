# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0067_auto_20150923_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invited',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('upline.member',),
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['name'], 'verbose_name': 'contato', 'verbose_name_plural': 'contatos'},
        ),
        migrations.AddField(
            model_name='event',
            name='alert_15_mins',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='alert_1_day',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='alert_1_hour',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='alert_2_hours',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='alert_30_mins',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='alert_5_mins',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='alert_at_hour',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to=b'thumbnails', null=True, verbose_name='thumbnail', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='thumbnail',
            field=models.ImageField(upload_to=b'thumbnails', null=True, verbose_name='thumbnail', blank=True),
        ),
    ]
