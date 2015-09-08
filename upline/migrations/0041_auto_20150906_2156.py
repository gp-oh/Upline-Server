# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0040_auto_20150904_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='level',
            options={'verbose_name': 'gradua\xe7\xe3o', 'verbose_name_plural': 'gradua\xe7\xf5es'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='owner',
            field=models.ForeignKey(related_name='contact_owner', verbose_name='upline', to='upline.Member'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='level',
            field=models.ForeignKey(verbose_name='gradua\xe7\xe3o', to='upline.Level'),
        ),
        migrations.AlterField(
            model_name='member',
            name='level',
            field=models.ForeignKey(verbose_name='gradua\xe7\xe3o', to='upline.Level', null=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='answer_type',
            field=models.IntegerField(verbose_name='tipo de resposta', choices=[(0, 'texto'), (1, '\xe1udio'), (2, 'video'), (3, 'lista'), (4, 'reuni\xe3o')]),
        ),
    ]
