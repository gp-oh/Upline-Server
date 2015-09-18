# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0056_level_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='image',
            field=models.ImageField(upload_to=b'levels', null=True, verbose_name='imagem', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='level',
            field=models.ForeignKey(default=1, editable=False, to='upline.Level', verbose_name='gradua\xe7\xe3o'),
        ),
    ]
