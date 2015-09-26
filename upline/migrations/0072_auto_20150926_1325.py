# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0071_sale_pontuated'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberTrainingStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField(verbose_name='resposta')),
                ('member', models.ForeignKey(related_name='training_steps', verbose_name='membro', to='upline.Member')),
                ('training_step', models.ForeignKey(related_name='members', verbose_name='etapa de treinamento', to='upline.TrainingStep')),
            ],
            options={
                'verbose_name': 'etapa de treinamento do membro',
                'verbose_name_plural': 'etapas de treinamento do membro',
            },
        ),
        migrations.RemoveField(
            model_name='membertraingstep',
            name='member',
        ),
        migrations.RemoveField(
            model_name='membertraingstep',
            name='training_step',
        ),
        migrations.DeleteModel(
            name='MemberTraingStep',
        ),
    ]
