# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0016_auto_20150819_1606'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MODELNAME',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_category',
            field=models.IntegerField(choices=[(0, b'Contato'), (1, b'Cliente')]),
        ),
        migrations.DeleteModel(
            name='ContactCategory',
        ),
    ]
