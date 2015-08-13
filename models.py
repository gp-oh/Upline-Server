# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    owner = models.ForeignKey('Member')
    member = models.ForeignKey('Member', blank=True, null=True)
    contact_category = models.ForeignKey('ContactCategory')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=45, blank=True, null=True)
    gender = models.IntegerField()
    postal_code = models.DecimalField(max_digits=10, decimal_places=0)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'


class ContactCategory(models.Model):
    title = models.CharField(unique=True, max_length=255)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_category'


class Goal(models.Model):
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goal'


class Level(models.Model):
    title = models.CharField(unique=True, max_length=255)
    points_range_from = models.DecimalField(max_digits=10, decimal_places=0)
    points_range_to = models.DecimalField(max_digits=10, decimal_places=0)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'level'


class LogMemberLogin(models.Model):
    member = models.ForeignKey('Member')
    ipv4_address = models.CharField(max_length=15, blank=True, null=True)
    ipv6_address = models.CharField(max_length=40, blank=True, null=True)
    agent = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_member_login'


class Member(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    external_id = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    active = models.IntegerField()
    binary = models.IntegerField()
    points = models.DecimalField(max_digits=10, decimal_places=0)
    avatar_url = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    gender = models.IntegerField()
    postal_code = models.DecimalField(max_digits=10, decimal_places=0)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=100)
    dream = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    level = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'member'


class MemberHasTrainingStep(models.Model):
    user = models.ForeignKey(Member)
    training_step = models.ForeignKey('TrainingStep')
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_has_training_step'
        unique_together = (('user_id', 'training_step_id'),)


class Training(models.Model):
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training'


class TrainingStep(models.Model):
    training = models.ForeignKey(Training)
    title = models.CharField(max_length=255)
    media_url = models.CharField(max_length=255, blank=True, null=True)
    step = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_step'
