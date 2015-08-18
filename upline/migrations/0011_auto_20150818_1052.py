# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0010_auto_20150818_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='avatar',
            field=models.ImageField(null=True, upload_to=b'contacts', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='training',
            field=models.ForeignKey(related_name='training_steps', to='upline.Training'),
        ),
    ]
