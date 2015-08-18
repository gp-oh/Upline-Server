# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0007_auto_20150817_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistributionCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'DistributionCenter',
                'verbose_name_plural': 'DistributionCenters',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('reference_value', models.DecimalField(max_digits=11, decimal_places=2)),
                ('table_value', models.DecimalField(max_digits=11, decimal_places=2)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('total', models.DecimalField(max_digits=11, decimal_places=2)),
                ('points', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
            },
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('total', models.DecimalField(max_digits=11, decimal_places=2)),
                ('delivery_prevision', models.DateField()),
                ('notificate_at', models.DateField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(to='upline.Product')),
                ('sale', models.ForeignKey(related_name='sale_items', to='upline.Sale')),
            ],
            options={
                'verbose_name': 'SaleItem',
                'verbose_name_plural': 'SaleItems',
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='cellphone',
            field=models.CharField(max_length=45, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='cpf',
            field=models.CharField(max_length=45, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='region',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='rg',
            field=models.CharField(max_length=45, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='client',
            field=models.ForeignKey(to='upline.Contact'),
        ),
        migrations.AddField(
            model_name='sale',
            name='member',
            field=models.ForeignKey(to='upline.Member'),
        ),
    ]
