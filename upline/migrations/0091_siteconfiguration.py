# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0090_event_parent_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('new_event_message', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('new_training_message', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('new_training_step_message', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('new_post_message', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('new_media_message', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('update_event_message', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('update_training_message', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('update_training_step_message', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('update_post_message', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('update_media_message', models.CharField(default=None, max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
        ),
    ]
