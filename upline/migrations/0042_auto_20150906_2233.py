# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0041_auto_20150906_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('audio', models.FileField(upload_to=b'audios')),
                ('converted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Audio',
                'verbose_name_plural': 'Audios',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video', models.FileField(upload_to=b'videos')),
                ('converted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.RemoveField(
            model_name='media',
            name='media_file',
        ),
        migrations.RemoveField(
            model_name='post',
            name='media',
        ),
        migrations.RemoveField(
            model_name='trainingstep',
            name='media',
        ),
        migrations.AddField(
            model_name='media',
            name='image',
            field=models.ImageField(upload_to=b'multimidida', null=True, verbose_name='imagem', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=b'posts', null=True, verbose_name='imagem', blank=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='image',
            field=models.ImageField(upload_to=b'training_steps', null=True, verbose_name='imagem', blank=True),
        ),
        migrations.AddField(
            model_name='media',
            name='audio',
            field=models.ForeignKey(default=None, blank=True, to='upline.Audio', null=True),
        ),
        migrations.AddField(
            model_name='media',
            name='video',
            field=models.ForeignKey(default=None, blank=True, to='upline.Video', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='audio',
            field=models.ForeignKey(default=None, blank=True, to='upline.Audio', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.ForeignKey(default=None, blank=True, to='upline.Video', null=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='audio',
            field=models.ForeignKey(default=None, blank=True, to='upline.Audio', null=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='video',
            field=models.ForeignKey(default=None, blank=True, to='upline.Video', null=True),
        ),
    ]
