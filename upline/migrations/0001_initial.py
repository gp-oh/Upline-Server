# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=45, null=True, blank=True)),
                ('gender', models.IntegerField()),
                ('postal_code', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255, null=True, blank=True)),
                ('state', models.CharField(max_length=255, null=True, blank=True)),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('points_range_from', models.IntegerField()),
                ('points_range_to', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LogMemberLogin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipv4_address', models.CharField(max_length=15, null=True, blank=True)),
                ('ipv6_address', models.CharField(max_length=40, null=True, blank=True)),
                ('agent', models.CharField(max_length=255, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('external_id', models.IntegerField(unique=True, null=True, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('points', models.IntegerField()),
                ('avatar_url', models.CharField(max_length=255, null=True, blank=True)),
                ('phone', models.CharField(max_length=45, null=True, blank=True)),
                ('gender', models.IntegerField()),
                ('postal_code', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255, null=True, blank=True)),
                ('state', models.CharField(max_length=255, null=True, blank=True)),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
                ('password', models.CharField(max_length=100)),
                ('dream', models.TextField(null=True, blank=True)),
                ('status', models.TextField(null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('level', models.ForeignKey(to='upline.Level')),
                ('parent', models.ForeignKey(blank=True, to='upline.Member', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField()),
                ('member', models.ForeignKey(related_name='team_member', to='upline.Member')),
                ('owner', models.ForeignKey(related_name='team_owner', to='upline.Member')),
            ],
            options={
                'verbose_name': 'MemberTeam',
                'verbose_name_plural': 'MemberTeams',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('media_url', models.CharField(max_length=255, null=True, blank=True)),
                ('step', models.IntegerField()),
                ('description', models.TextField(null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('training', models.ForeignKey(to='upline.Training')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='training_steps',
            field=models.ManyToManyField(to='upline.TrainingStep'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='logmemberlogin',
            name='member',
            field=models.ForeignKey(to='upline.Member'),
        ),
        migrations.AddField(
            model_name='goal',
            name='level',
            field=models.ForeignKey(to='upline.Level'),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_category',
            field=models.ForeignKey(to='upline.ContactCategory'),
        ),
        migrations.AddField(
            model_name='contact',
            name='member',
            field=models.ForeignKey(related_name='contact_member', blank=True, to='upline.Member', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='owner',
            field=models.ForeignKey(related_name='contact_owner', to='upline.Member'),
        ),
    ]
