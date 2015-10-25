# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0091_siteconfiguration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='new_training_step_message',
        ),
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='update_training_step_message',
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='new_event_message',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Mensagem de novo evento', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='new_media_message',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Mensagem de nova m\xeddia', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='new_post_message',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Mensagem de nova not\xedcia', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='new_training_message',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Mensagem de novo treinamento', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='update_event_message',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Mensagem de evento alterado', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='update_media_message',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Mensagem de altera\xe7\xe3o de m\xeddia', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='update_post_message',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Mensagem de altera\xe7\xe3o not\xedcia', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='update_training_message',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Mensagem de altera\xe7\xe3o de treinamento', blank=True),
        ),
    ]
