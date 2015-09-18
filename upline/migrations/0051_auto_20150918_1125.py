# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0050_auto_20150917_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='day_14_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 14', blank=True),
        ),
        migrations.AddField(
            model_name='training',
            name='day_1_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 1', blank=True),
        ),
        migrations.AddField(
            model_name='training',
            name='day_28_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 28', blank=True),
        ),
        migrations.AddField(
            model_name='training',
            name='day_2_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 2', blank=True),
        ),
        migrations.AddField(
            model_name='training',
            name='day_3_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 3', blank=True),
        ),
        migrations.AddField(
            model_name='training',
            name='day_4_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 4', blank=True),
        ),
        migrations.AddField(
            model_name='training',
            name='day_5_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 5', blank=True),
        ),
        migrations.AddField(
            model_name='training',
            name='day_6_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 6', blank=True),
        ),
        migrations.AddField(
            model_name='training',
            name='day_7_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 7', blank=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='group',
            field=models.ForeignKey(verbose_name='prupo', to='auth.Group', null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='level',
            field=models.ForeignKey(verbose_name='gradua\xe7\xe3o', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(max_length=255, verbose_name='mensagem'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='sent',
            field=models.BooleanField(default=False, verbose_name='enviado', editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(verbose_name='prupo', to='auth.Group', null=True),
        ),
    ]
