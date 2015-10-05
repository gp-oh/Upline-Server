# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0076_auto_20151004_1050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-create_time'], 'verbose_name': 'not\xedcia', 'verbose_name_plural': 'not\xedcias'},
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='outpooring',
            field=models.IntegerField(default=0, verbose_name='derramamento', choices=[(0, b'Esquerda'), (1, b'Direita')]),
        ),
    ]
