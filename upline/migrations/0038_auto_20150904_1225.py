# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('upline', '0037_auto_20150903_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='level',
        ),
        migrations.AddField(
            model_name='level',
            name='group',
            field=models.ForeignKey(verbose_name='grupo', to='auth.Group', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(verbose_name='grupo', to='auth.Group', null=True),
        ),
    ]
