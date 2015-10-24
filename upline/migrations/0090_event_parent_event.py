# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0089_event_inviter'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='parent_event',
            field=models.ForeignKey(default=None, blank=True, to='upline.Event', null=True),
        ),
    ]
