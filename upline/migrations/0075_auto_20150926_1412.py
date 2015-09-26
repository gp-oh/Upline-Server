# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0074_trainingstep_media_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membertrainingstep',
            name='member',
            field=models.ForeignKey(related_name='answers', verbose_name='membro', to='upline.Member'),
        ),
    ]
