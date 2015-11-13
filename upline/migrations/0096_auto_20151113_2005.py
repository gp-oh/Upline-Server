# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0095_auto_20151113_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteconfiguration',
            old_name='first_training_id',
            new_name='first_training',
        ),
    ]
