# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0014_auto_20150818_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Citys',
            },
        ),
        migrations.CreateModel(
            name='PostalCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('street_type', models.CharField(max_length=255)),
                ('approved', models.BooleanField(default=False)),
                ('city', models.ForeignKey(to='upline.City')),
            ],
            options={
                'verbose_name': 'Postal Code',
                'verbose_name_plural': 'Postal Codes',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acronym', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
            },
        ),
        migrations.DeleteModel(
            name='DistributionCenter',
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='upline.State'),
        ),
    ]
