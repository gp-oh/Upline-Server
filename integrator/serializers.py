from django.contrib.auth.models import User, Group
from upline.models import *
from rest_framework import serializers
from django.core.files.uploadedfile import SimpleUploadedFile
import mimetypes, json, base64, uuid

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ("id", 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id",'username', 'email')

class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ("id","acronym","name",)

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ("id","state","name",)

class PostalCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostalCode
        fields = ("id","city","street","neighborhood","postal_code","street_type","approved",)

class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training
        fields = ("id","name","create_time","update_time","have_notifications","count_messages_after_finish","day_1_notification_description","day_2_notification_description","day_3_notification_description","day_4_notification_description","day_5_notification_description","day_6_notification_description","day_7_notification_description","day_14_notification_description","day_28_notification_description",)

class TrainingStepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainingStep
        fields = ("id","training","title","media","thumbnail","step","description","need_answer","answer_type","meetings_per_week","weeks","nr_contacts","have_notifications","day_1_notification_description","day_2_notification_description","day_3_notification_description","day_4_notification_description","day_5_notification_description","day_6_notification_description","day_7_notification_description","day_14_notification_description","day_28_notification_description","create_time","update_time",)

class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ("id","title","image","color","description","gift","group","points_range_from","points_range_to","create_time","update_time",)

class MemberTraingStepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MemberTraingStep
        fields = ("id","member","training_step","answer",)

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ("id","member_uid","user","parent","external_id","name","quickblox_id","quickblox_password","points","avatar","phone","gender","postal_code","city","state","address","address_number","dream1","dream2","status","birthday","level","outpooring","create_time","update_time",)

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ("id",)

class GoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        fields = ("id",)

class LogMemberLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LogMemberLogin
        fields = ("id",)

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ("id",)

class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sale
        fields = ("id",)

class SaleItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SaleItem
        fields = ("id",)

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ("id",)

class CalendarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calendar
        fields = ("id",)

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ("id",)

class EventAlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventAlert
        fields = ("id",)

class MediaCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MediaCategory
        fields = ("id",)

class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = ("id",)

class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ("id",)
