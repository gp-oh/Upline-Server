# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand, CommandError
from push_notifications.models import *
from upline.models import *


class Command(BaseCommand):
    help = 'Clean the database'

    def handle(self, *args, **options):
        MemberTrainingStep.objects.all().delete()
        Avatar.objects.all().delete()
        TrainingStep.objects.all().delete()
        Training.objects.all().delete()
        Contact.objects.all().delete()
        Invite.objects.all().delete()
        Goal.objects.all().delete()
        SaleItem.objects.all().delete()
        Sale.objects.all().delete()
        Product.objects.all().delete()
        Level.objects.all().delete()
        LogMemberLogin.objects.all().delete()
        Post.objects.all().delete()
        EventAlert.objects.all().delete()
        Event.objects.all().delete()
        Calendar.objects.all().delete()
        Media.objects.all().delete()
        MediaCategory.objects.all().delete()
        Notification.objects.all().delete()
        Binary.objects.all().delete()
        GCMDevice.objects.all().delete()
        APNSDevice.objects.all().delete()
        Member.objects.all().delete()
        User.objects.all().delete()
        Group.objects.all().delete()
        self.stdout.write('Cleaned Database')
