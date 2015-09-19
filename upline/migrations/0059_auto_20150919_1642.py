# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0058_auto_20150918_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAlert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alert_date', models.DateTimeField(default=None, null=True, blank=True)),
                ('event', models.ForeignKey(to='upline.Event')),
            ],
            options={
                'verbose_name': 'EventAlert',
                'verbose_name_plural': 'EventAlerts',
            },
        ),
        migrations.RemoveField(
            model_name='calendar',
            name='public',
        ),
        migrations.RemoveField(
            model_name='calendar',
            name='user',
        ),
        migrations.AddField(
            model_name='calendar',
            name='color',
            field=colorful.fields.RGBColorField(default=b'#ffffff'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(verbose_name='thumbnail', upload_to=b'thumbnails', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='answer_type',
            field=models.IntegerField(verbose_name='tipo de resposta', choices=[(0, 'texto'), (1, '\xe1udio'), (2, 'video'), (5, 'imagem'), (3, 'lista'), (4, 'reuni\xe3o')]),
        ),
    ]
