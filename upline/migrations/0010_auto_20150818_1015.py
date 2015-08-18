# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0009_member_quickblox_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberTraingStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name': 'MemberTraingStep',
                'verbose_name_plural': 'MemberTraingSteps',
            },
        ),
        migrations.RemoveField(
            model_name='member',
            name='training_steps',
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='need_answer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='membertraingstep',
            name='member',
            field=models.ForeignKey(related_name='training_steps', to='upline.Member'),
        ),
        migrations.AddField(
            model_name='membertraingstep',
            name='training_step',
            field=models.ForeignKey(related_name='members', to='upline.TrainingStep'),
        ),
    ]
