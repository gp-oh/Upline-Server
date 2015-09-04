# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
# import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0029_saleitem_notified'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='tree_id',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='answer_type',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='day_14_notification_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='day_1_notification_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='day_28_notification_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='day_2_notification_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='day_3_notification_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='day_4_notification_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='day_5_notification_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='day_6_notification_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='day_7_notification_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='meetings_per_week',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='nr_contacts',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainingstep',
            name='weeks',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        # migrations.AlterField(
        #     model_name='member',
        #     name='parent',
        #     field=mptt.fields.TreeForeignKey(related_name='downlines', blank=True, to='upline.Member', null=True),
        # ),
    ]
