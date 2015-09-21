# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0061_auto_20150919_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='member',
        ),
        migrations.RemoveField(
            model_name='team',
            name='owner',
        ),
        migrations.AlterModelOptions(
            name='eventalert',
            options={'verbose_name': 'alerta do evento', 'verbose_name_plural': 'alertas do evento'},
        ),
        migrations.AddField(
            model_name='city',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 21, 34, 14, 773661), verbose_name='data de cria\xe7\xe3o', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 21, 34, 21, 92415), verbose_name='data de altera\xe7\xe3o', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postalcode',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 21, 34, 23, 972308), verbose_name='data de cria\xe7\xe3o', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postalcode',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 21, 34, 27, 928280), verbose_name='data de altera\xe7\xe3o', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 21, 34, 31, 148387), verbose_name='data de cria\xe7\xe3o', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 21, 34, 32, 764105), verbose_name='data de altera\xe7\xe3o', auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='address_number',
            field=models.CharField(max_length=255, null=True, verbose_name='n\xfamero', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='postal_code',
            field=models.CharField(max_length=255, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='event',
            name='group',
            field=models.ForeignKey(default=None, blank=True, to='auth.Group', null=True, verbose_name='grupo'),
        ),
        migrations.AlterField(
            model_name='event',
            name='postal_code',
            field=models.CharField(max_length=255, null=True, verbose_name='CEP', blank=True),
        ),
        migrations.AlterField(
            model_name='eventalert',
            name='alert_date',
            field=models.DateTimeField(default=None, null=True, verbose_name='data do alerta', blank=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='group',
            field=models.ForeignKey(editable=False, to='auth.Group', null=True, verbose_name='grupo'),
        ),
        migrations.AlterField(
            model_name='media',
            name='converted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='address_number',
            field=models.CharField(max_length=255, null=True, verbose_name='n\xfamero', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='postal_code',
            field=models.CharField(max_length=255, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(help_text='255 caracteres', max_length=255, verbose_name='mensagem'),
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(verbose_name='grupo', to='auth.Group', null=True),
        ),
        migrations.AlterField(
            model_name='postalcode',
            name='postal_code',
            field=models.CharField(max_length=255, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='training',
            name='count_messages_after_finish',
            field=models.ForeignKey(verbose_name='treinamentos anteriores', to='upline.Training', null=True),
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
