# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0022_event_owner'),
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
        migrations.AddField(
            model_name='multimidia',
            name='media_file',
            field=models.FileField(default='', upload_to=b'multimidida'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='multimidia',
            name='media_type',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='multimidia',
            name='multimidia_category',
            field=models.ForeignKey(related_name='medias', default='', to='upline.MultimidiaCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='multimidia',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='multimidiacategory',
            name='multimidia_type',
            field=models.ForeignKey(related_name='categories', default='', to='upline.MultimidiaType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='multimidiacategory',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='multimidiatype',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
