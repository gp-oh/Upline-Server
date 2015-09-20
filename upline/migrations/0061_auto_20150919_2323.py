# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('upline', '0060_post_media_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='group',
            field=models.ForeignKey(default=None, blank=True, to='auth.Group', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='media_type',
            field=models.IntegerField(default=0, verbose_name='tipo de midia', editable=False, choices=[(0, b'Imagem'), (1, b'Audio'), (2, b'Video')]),
        ),
    ]
