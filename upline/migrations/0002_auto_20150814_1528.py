# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='contactcategory',
            options={'verbose_name': 'Contact Category', 'verbose_name_plural': 'Contact Categorys'},
        ),
        migrations.AlterModelOptions(
            name='goal',
            options={'verbose_name': 'Goal', 'verbose_name_plural': 'Goals'},
        ),
        migrations.AlterModelOptions(
            name='level',
            options={'verbose_name': 'Level', 'verbose_name_plural': 'Levels'},
        ),
        migrations.AlterModelOptions(
            name='logmemberlogin',
            options={'verbose_name': 'Log Member Login', 'verbose_name_plural': 'Log Member Logins'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'Member', 'verbose_name_plural': 'Members'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Member Team', 'verbose_name_plural': 'Member Teams'},
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'verbose_name': 'Training', 'verbose_name_plural': 'Trainings'},
        ),
        migrations.AlterModelOptions(
            name='trainingstep',
            options={'verbose_name': 'Training Step', 'verbose_name_plural': 'Training Steps'},
        ),
        migrations.AddField(
            model_name='goal',
            name='member',
            field=models.ForeignKey(default=1, to='upline.Member'),
            preserve_default=False,
        ),
    ]
