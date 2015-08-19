# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upline', '0015_auto_20150818_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multimidia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Multimidia',
                'verbose_name_plural': 'Multimidias',
            },
        ),
        migrations.CreateModel(
            name='MultimidiaCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'MultimidiaCategory',
                'verbose_name_plural': 'MultimidiaCategorys',
            },
        ),
        migrations.CreateModel(
            name='MultimidiaType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'MultimidiaType',
                'verbose_name_plural': 'MultimidiaTypes',
            },
        ),
        migrations.RemoveField(
            model_name='member',
            name='dream',
        ),
        migrations.AddField(
            model_name='calendar',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='calendar',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='dream1',
            field=models.ImageField(default=None, null=True, upload_to=b'dreams', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='dream2',
            field=models.ImageField(default=None, null=True, upload_to=b'dreams', blank=True),
        ),
    ]
