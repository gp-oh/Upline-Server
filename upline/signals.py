from django.db.models.signals import post_save, m2m_changed, pre_delete
from django.dispatch import receiver
from upline.models import *
from upline.serializers import *

def push_event(sender, instance, created, **kwargs):
    devices = GCMDevice.objects.filter(user=instance.owner)
    if len(devices) > 0:
        devices.send_message(SiteConfiguration.get_solo().new_event_message if created else SiteConfiguration.get_solo().update_event_message , extra={"event":EventSerializer(instance, many=False).data})

post_save.connect(push_event, sender=Event, dispatch_uid="push_event")


def push_delete_event(sender, instance, **kwargs):
    devices = GCMDevice.objects.filter(user=instance.owner)
    if len(devices) > 0:
        devices.send_message(None, extra={"event":EventDeleteSerializer(instance, many=False).data})

pre_delete.connect(push_delete_event, sender=Event, dispatch_uid="push_event")


@receiver(m2m_changed, sender=Event.members.through)
def recalculate_total(sender, instance, action, **kwargs):
    """
    Automatically recalculate total price of an order when a related product is added or removed
    """

    if action == "post_add" and not instance.is_invited:
        members = instance.members.all()
        users = []
        for member in members:
            users.append(member.user)
        related_events = Event.objects.filter(parent_event=instance)
        exclude_events = related_events.exclude(owner__in=users)
        related_event_users = []
        create_event_users = []
        for event in related_events:
            related_event_users.append(event.owner)
        for user in users:
            if user not in related_event_users:
                create_event_users.append(user)
        instance_id = instance.id
        for user in create_event_users:
            e = instance
            e.id = None
            e.owner = user
            e.is_invited = True
            e.parent_event_id = instance_id
            e.alert_at_hour = False
            e.alert_5_mins = False
            e.alert_15_mins = False
            e.alert_30_mins = False
            e.alert_1_hour = False
            e.alert_2_hours = False
            e.alert_1_day = False
            e.inviter = Member.objects.get(user=instance.owner)
            e.save()

        for event in exclude_events:
            event.delete()

        for event in related_events:
            if event not in exclude_events:
                event.group = instance.group
                event.title = instance.title
                event.all_day = instance.all_day
                event.begin_time = instance.begin_time
                event.end_time = instance.end_time
                event.calendar = instance.calendar
                event.note = instance.note
                event.postal_code = instance.postal_code
                event.region = instance.region
                event.city = instance.city
                event.state = instance.state
                event.address = instance.address
                event.address_number = instance.address_number
                event.complement = instance.complement
                event.lat = instance.lat
                event.lng = instance.lng
                # event.alert_at_hour = instance.event
                # event.alert_5_mins = instance.event
                # event.alert_15_mins = instance.event
                # event.alert_30_mins = instance.event
                # event.alert_1_hour = instance.event
                # event.alert_2_hours = instance.event
                # event.alert_1_day = instance.event
                event.save()




