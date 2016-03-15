from django.core.management.base import BaseCommand, CommandError
from push_notifications.models import GCMDevice
from upline.models import *
from upline.serializers import TrainingStepTaskSerializer, SaleItemSerializer, SaleSerializer
import datetime
import pytz
from django.conf import settings


class Command(BaseCommand):
    help = 'Send marketing notifications'

    #def notify_sale_items(self):
    #    sales = Sale.objects.all().order_by('member__id').distinct('member__id')
    #    for sale in sales:
    #      devices = GCMDevice.objects.filter(user=sale.member.user)
    #      message = 'Sale item done!'
    #      if len(devices) > 0:
    #         devices.send_message(message, extra={
    #                                     "type": "sale", "object": SaleSerializer(sale,many=False).data})
        

    def notify_late_tranings(self):
        last_training_steps = MemberTrainingStep.objects.all().order_by('member__id', '-training_step__training__position',
                                                                        '-training_step__step').distinct('member__id')
        print last_training_steps
        tz = pytz.timezone(settings.TIME_ZONE)
        for training_step in last_training_steps:
            next_training_step = training_step.training_step.next_training_step()
            if next_training_step and next_training_step.have_notifications:
                time_distance = (tz.localize(datetime.datetime.today(), is_dst=None).astimezone(pytz.utc) -
                                 training_step.update_time).days
                print 'dias'
                print time_distance
                message = ''
                if time_distance <= 1:
                    message = next_training_step.day_1_notification_description
                elif time_distance == 2:
                    message = next_training_step.day_2_notification_description
                elif time_distance == 3:
                    message = next_training_step.day_3_notification_description
                elif time_distance == 4:
                    message = next_training_step.day_4_notification_description
                elif time_distance == 5:
                    message = next_training_step.day_5_notification_description
                elif time_distance == 6:
                    message = next_training_step.day_6_notification_description
                elif time_distance == 7:
                    message = next_training_step.day_7_notification_description
                elif time_distance == 14:
                    message = next_training_step.day_14_notification_description
                elif time_distance == 28:
                    message = next_training_step.day_28_notification_description

                devices = GCMDevice.objects.filter(
                    user=training_step.member.user)
                if len(devices) > 0 and message != '':
                    devices.send_message(message, extra={
                                         "type": "training_step_task", "object": TrainingStepTaskSerializer(next_training_step, many=False).data})

    def notify_unstarted_trainigs(self):
        members = Member.objects.filter(member_type=0).exclude(id__in=MemberTrainingStep.objects.values_list(
            'member__id', flat=True).distinct('member__id'))

        print members
        tz = pytz.timezone(settings.TIME_ZONE)
        next_training_step = TrainingStep.objects.all(
        ).order_by('training__position', 'step')[0]
        for member in members:
            time_distance = (tz.localize(datetime.datetime.today(), is_dst=None).astimezone(pytz.utc) -
                             member.create_time).days

            message = ''
            if time_distance <= 1:
                message = next_training_step.day_1_notification_description
            elif time_distance == 2:
                message = next_training_step.day_2_notification_description
            elif time_distance == 3:
                message = next_training_step.day_3_notification_description
            elif time_distance == 4:
                message = next_training_step.day_4_notification_description
            elif time_distance == 5:
                message = next_training_step.day_5_notification_description
            elif time_distance == 6:
                message = next_training_step.day_6_notification_description
            elif time_distance == 7:
                message = next_training_step.day_7_notification_description
            elif time_distance == 14:
                message = next_training_step.day_14_notification_description
            elif time_distance == 28:
                message = next_training_step.day_28_notification_description

            devices = GCMDevice.objects.filter(
                user=member.user)
            if len(devices) > 0 and message != '':
                devices.send_message(message, extra={
                                     "type": "training_step_task", "object": TrainingStepTaskSerializer(next_training_step, many=False).data})

    def handle(self, *args, **options):
        self.notify_late_tranings()
        self.notify_unstarted_trainigs()
        #self.notify_sale_items()
        self.stdout.write('Successfully send notifications')
