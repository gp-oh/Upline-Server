# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0104_auto_20160527_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='groups',
            field=models.ManyToManyField(default=None, to='auth.Group', verbose_name='grupos', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.OneToOneField(related_name='member_user', verbose_name='usu\xe1rio', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='groups',
            field=models.ManyToManyField(default=None, to='auth.Group', verbose_name='grupos', blank=True),
        ),
    ]
