# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0023_auto_20150822_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('media_type', models.IntegerField()),
                ('media_file', models.FileField(upload_to=b'multimidida')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Medias',
            },
        ),
        migrations.RenameModel(
            old_name='MultimidiaCategory',
            new_name='MediaCategory',
        ),
        migrations.RenameModel(
            old_name='MultimidiaType',
            new_name='MediaType',
        ),
        migrations.RemoveField(
            model_name='multimidia',
            name='multimidia_category',
        ),
        migrations.AlterModelOptions(
            name='mediacategory',
            options={'verbose_name': 'MediaCategory', 'verbose_name_plural': 'MediaCategorys'},
        ),
        migrations.AlterModelOptions(
            name='mediatype',
            options={'verbose_name': 'MediaType', 'verbose_name_plural': 'MediaTypes'},
        ),
        migrations.RenameField(
            model_name='mediacategory',
            old_name='multimidia_type',
            new_name='media_type',
        ),
        migrations.DeleteModel(
            name='Multimidia',
        ),
        migrations.AddField(
            model_name='media',
            name='media_category',
            field=models.ForeignKey(related_name='medias', to='upline.MediaCategory'),
        ),
    ]
