# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0018_auto_20150822_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='place',
        ),
        migrations.AddField(
            model_name='event',
            name='complement',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='lat',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='lng',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='number',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='postal_code',
            field=models.ForeignKey(default=None, blank=True, to='upline.PostalCode', null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='quickblox_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='total',
            field=models.DecimalField(default=b'0.00', max_digits=11, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='total',
            field=models.DecimalField(default=b'0.00', max_digits=11, decimal_places=2),
        ),
        migrations.DeleteModel(
            name='Place',
        ),
    ]
