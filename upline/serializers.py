# -*- coding: utf-8 -*-
import base64
import datetime
import uuid

from django.contrib.auth.models import Group, User
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import serializers
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin
from upline.models import *


class UTCDateTimeField(serializers.DateTimeField):

    def to_representation(self, value):
        if self.format is None:
            return value
        value = value.isoformat()
        return value


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ("id", 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)
    avatar = serializers.SerializerMethodField()

    def get_avatar(self, user):
        avatar = Avatar.objects.filter(user=user)
        if len(avatar) > 0:
            return avatar[0].image.url
        else:
            return None

    class Meta:
        model = User
        fields = ("id", 'groups', 'username', 'email', "avatar")


class UsernameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username')


class LevelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Level
        fields = ("id", "title", "image", "color", "description",
                  "gift", "points_range_from", "points_range_to")


class OnlyTrainingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Training
        fields = ("id", 'name',)


class TrainingStepLoginSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TrainingStep
        fields = ('id', 'title', 'media', "thumbnail", "media_type", 'step', 'description',
                  'need_answer', "answer_type", "meetings_per_week", "weeks", "nr_contacts")


class TrainingStepSerializer(serializers.HyperlinkedModelSerializer):
    status = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    def get_status(self, training_step):
        members = training_step.members.filter(
            member__user=self.context['request'].user)
        if len(members) > 0:
            return True
        return False

    def get_answer(self, training_step):
        members = training_step.members.filter(
            member__user=self.context['request'].user)
        if len(members) > 0:
            return MemberTrainingStepSerializer(members[0]).data
        return None

    class Meta:
        model = TrainingStep
        fields = ('id', 'status', 'answer', 'title', 'media', "thumbnail", "media_type", 'step',
                  'description', 'need_answer', "answer_type", "meetings_per_week", "weeks", "nr_contacts")


class TrainingStepTaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TrainingStep
        fields = ('id', 'title', 'media', "thumbnail", "media_type", 'step',
                  'description', 'need_answer', "answer_type", "meetings_per_week", "weeks", "nr_contacts")


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    training_steps = TrainingStepSerializer(many=True, read_only=True)

    class Meta:
        model = Training
        fields = ('id', 'name', 'training_steps')


class MemberTrainingStepSerializer(serializers.HyperlinkedModelSerializer):
    training_step = serializers.PrimaryKeyRelatedField(
        many=False, queryset=TrainingStep.objects.all())
    # training_step = TrainingSetpSerializer(many=False,read_only=True)
    media_base64 = serializers.CharField(
        write_only=True, required=False, allow_blank=True)

    def create(self, validated_data):
        validated_data['member'] = Member.objects.get(
            user=self.context['request'].user)
        return super(MemberTrainingStepSerializer, self).create(validated_data)

    def save(self):
        print self.validated_data
        if 'media_base64' in self.validated_data:
            media = self.validated_data.pop('media_base64')
            if len(media) > 0:
                media_base64 = media.split(',')[1]
                media_mime = media.split(';')[0].split(':')[1]
                media_extension = media_mime.split('/')[1]
                self.media = SimpleUploadedFile(name=str(uuid.uuid4(
                )) + '.' + media_extension, content=base64.b64decode(media_base64), content_type=media_mime)
        super(MemberTrainingStepSerializer, self).save()

    class Meta:
        model = MemberTrainingStep
        fields = ('id', 'answer', 'training_step', 'media', 'media_base64')


class UplineSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    level = LevelSerializer(many=False, read_only=True)
    answers = serializers.SerializerMethodField()
    descendant_count = serializers.SerializerMethodField()
    downline_count = serializers.SerializerMethodField()
    binary = serializers.SerializerMethodField()
    today_descendant_count = serializers.SerializerMethodField()

    def get_answers(self, member):
        answers = MemberTrainingStep.objects.select_related(
            'training_step').filter(member=member)
        ret = []
        for answer in answers:
            ret.append(answer.training_step.id)
        return ret

    def get_today_descendant_count(self, member):
        today_min = datetime.datetime.combine(
            datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(
            datetime.date.today(), datetime.time.max)
        return len(member.get_descendants().filter(create_time__range=(today_min, today_max), member_type=0))

    def get_descendant_count(self, member):
        return len(member.get_descendants().filter(member_type=0))

    def get_downline_count(self, member):
        return len(member.get_children())

    def get_binary(self, member):
        if len(member.get_children().filter(member_type=0)) < 2:
            return False
        else:
            return True

    class Meta:
        model = Member
        fields = ("id", "descendant_count", "today_descendant_count", "binary", "downline_count", "member_type", "user", 'quickblox_id', 'create_time', 'external_id', 'name',
                  'points', 'avatar', 'phone', 'gender', 'postal_code', 'city', 'state', 'address', 'address_number', 'dream1', 'dream2', 'status', 'level', 'answers', 'birthday')


class DownlineSerializer(serializers.HyperlinkedModelSerializer):
    level = LevelSerializer(many=False, read_only=True)
    answers = serializers.SerializerMethodField()
    downline_count = serializers.SerializerMethodField()
    binary = serializers.SerializerMethodField()
    descendant_count = serializers.SerializerMethodField()
    today_descendant_count = serializers.SerializerMethodField()

    def get_answers(self, member):
        answers = MemberTrainingStep.objects.select_related(
            'training_step').filter(member=member)
        ret = []
        for answer in answers:
            ret.append(answer.training_step.id)
        return ret

    def get_today_descendant_count(self, member):
        today_min = datetime.datetime.combine(
            datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(
            datetime.date.today(), datetime.time.max)
        return len(member.get_descendants().filter(create_time__range=(today_min, today_max), member_type=0))

    def get_downline_count(self, member):
        return len(member.get_children())

    def get_descendant_count(self, member):
        return len(member.get_descendants().filter(member_type=0))

    def get_binary(self, member):
        if len(member.get_children().filter(member_type=0)) < 2:
            return False
        else:
            return True

    class Meta:
        model = Member
        fields = ("id", "descendant_count", "today_descendant_count", "binary", "downline_count", "member_type", 'quickblox_id', 'create_time', 'external_id', 'name',
                  'points', 'avatar', 'phone', 'gender', 'postal_code', 'city', 'state', 'address', 'address_number', 'dream1', 'dream2', 'status', 'level', 'answers')


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    level = LevelSerializer(many=False, read_only=True)
    answers = serializers.SerializerMethodField()
    parent = UplineSerializer(many=False, read_only=True)
    downlines = serializers.SerializerMethodField(read_only=True)
    avatar_base64 = serializers.CharField(required=False, allow_blank=True)
    dream1_base64 = serializers.CharField(required=False, allow_blank=True)
    dream2_base64 = serializers.CharField(required=False, allow_blank=True)
    descendant_count = serializers.SerializerMethodField()
    downline_count = serializers.SerializerMethodField()
    binary = serializers.SerializerMethodField()
    today_descendant_count = serializers.SerializerMethodField()

    def get_downlines(self, obj):
        user = self.context['request'].user
        downlines = Member.objects.filter(parent=obj, member_type=0)
        # downlines = obj.get_descendants()
        serializer = DownlineSerializer(downlines, many=True)
        return serializer.data

    def get_answers(self, member):
        answers = MemberTrainingStep.objects.select_related(
            'training_step').filter(member=member)
        ret = []
        for answer in answers:
            ret.append(answer.training_step.id)
        return ret

    def get_today_descendant_count(self, member):
        today_min = datetime.datetime.combine(
            datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(
            datetime.date.today(), datetime.time.max)
        return len(member.get_descendants().filter(create_time__range=(today_min, today_max), member_type=0))

    def get_descendant_count(self, member):
        return len(member.get_descendants().filter(member_type=0))

    def get_downline_count(self, member):
        return len(member.get_children())

    def get_binary(self, member):
        if len(member.get_children().filter(member_type=0)) < 2:
            return False
        else:
            return True

    class Meta:
        model = Member
        fields = ("id", "descendant_count", 'email', "today_descendant_count", "binary", "downline_count", "member_type", "user", "avatar_base64", "dream1_base64", "dream2_base64", "avatar_base64", 'quickblox_id', 'parent',
                  'downlines', 'create_time', 'external_id', 'name', 'points', 'avatar', 'phone', 'gender', 'postal_code', 'city', 'state', 'address', 'address_number', 'dream1', 'dream2', 'status', 'level', 'answers', 'birthday')


class MemberRegisterSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.SlugField()
    email = serializers.EmailField()
    grant_type = serializers.CharField(initial="password")
    password = serializers.CharField(style={'input_type': 'password'})
    parent_user = serializers.SlugField()
    avatar_base64 = serializers.CharField(required=False, allow_blank=True)
    dream1_base64 = serializers.CharField(required=False, allow_blank=True)
    dream2_base64 = serializers.CharField(required=False, allow_blank=True)

    def validate_parent_user(self, value):
        members = Member.objects.filter(user__username=value, member_type=0)
        if len(members) != 1:
            raise serializers.ValidationError("Invalid Parent ID")
        return value

    def validate_email(self, value):
        users = User.objects.filter(email=value)
        if len(users) > 0:
            raise serializers.ValidationError("Email already registered")
        return value

    def validate_username(self, value):
        users = User.objects.filter(username=value)
        if len(users) > 0:
            raise serializers.ValidationError("Username already registered")
        return value

    def save(self):
        user = User()
        user.username = self.validated_data['username']
        user.email = self.validated_data['email']
        user.set_password(self.validated_data['password'])
        user.save()
        user.groups.add(Group.objects.get(id=3))
        user.save()

        member = Member()
        if 'avatar_base64' in self.validated_data:
            avatar = self.validated_data.pop('avatar_base64')
            if len(avatar) > 0:
                avatar_base64 = avatar.split(',')[1]
                avatar_mime = avatar.split(';')[0].split(':')[1]
                avatar_extension = avatar_mime.split('/')[1]
                member.avatar = SimpleUploadedFile(name=str(uuid.uuid4(
                )) + '.' + avatar_extension, content=base64.b64decode(avatar_base64), content_type=avatar_mime)
        if 'dream1_base64' in self.validated_data:
            dream1 = self.validated_data.pop('dream1_base64')
            if len(dream1) > 0:
                dream1_base64 = dream1.split(',')[1]
                dream1_mime = dream1.split(';')[0].split(':')[1]
                dream1_extension = dream1_mime.split('/')[1]
                self.dream1 = SimpleUploadedFile(name=str(uuid.uuid4(
                )) + '.' + dream1_extension, content=base64.b64decode(dream1_base64), content_type=dream1_mime)
        if 'dream2_base64' in self.validated_data:
            dream2 = self.validated_data.pop('dream2_base64')
            if len(dream2) > 0:
                dream2_base64 = dream2.split(',')[1]
                dream2_mime = dream2.split(';')[0].split(':')[1]
                dream2_extension = dream2_mime.split('/')[1]
                self.dream2 = SimpleUploadedFile(name=str(uuid.uuid4(
                )) + '.' + dream2_extension, content=base64.b64decode(dream2_base64), content_type=dream2_mime)

        member.parent = Member.objects.get(
            user__username=self.validated_data['parent_user'])
        member.member_type = 1

        if 'name' in self.validated_data:
            member.name = self.validated_data['name']
        if 'email' in self.validated_data:
            member.email = self.validated_data['email']
        if 'phone' in self.validated_data:
            member.phone = self.validated_data['phone']
        if 'gender' in self.validated_data:
            member.gender = self.validated_data['gender']
        if 'postal_code' in self.validated_data:
            member.postal_code = self.validated_data['postal_code']
        if 'birthday' in self.validated_data:
            member.birthday = self.validated_data['birthday']
        if 'state' in self.validated_data:
            member.state = self.validated_data['state']
        if 'city' in self.validated_data:
            member.city = self.validated_data['city']
        if 'address' in self.validated_data:
            member.address = self.validated_data['address']
        if 'address_number' in self.validated_data:
            member.address_number = self.validated_data['address_number']
        member.user = user
        member.save()

    class Meta:
        model = Member
        fields = ("id", "member_type", 'avatar_base64', "dream1_base64", "dream2_base64", 'name', 'email', 'grant_type', 'parent_user',
                  'username', 'password', 'phone', 'birthday', 'gender', 'postal_code', 'state', 'city', 'address', 'address_number')

# class MemberSerializer(serializers.HyperlinkedModelSerializer):
#     user = UserSerializer(many=False,read_only=True)
#     level = LevelSerializer(many=False, read_only=True)
#     answers = serializers.SerializerMethodField()
#     parent = UplineSerializer(many=False, read_only=True)
#     downlines = erializers.SerializerMethodField(read_only=True)
#     avatar_base64 = serializers.CharField(write_only=True,required=False,allow_blank=True)
#     descendant_count = serializers.SerializerMethodField()
#     downline_count = serializers.SerializerMethodField()
#     binary = serializers.SerializerMethodField()
#     today_descendant_count = serializers.SerializerMethodField()

#     def get_downlines(self, obj):
#         user = self.context['request'].user
#         downlines = Member.objects.filter(parent=obj,member_type=0)
#         serializer = DownlineSerializer(downlines,many=True)
#         return serializer.data

#     def get_answers(self,member):
#         answers = MemberTrainingStep.objects.select_related('training_step').filter(member=member)
#         ret = []
#         for answer in answers:
#             ret.append(answer.training_step.id)
#         return ret

#     def get_today_descendant_count(self,member):
#         today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
#         today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
# return
# len(member.get_descendants().filter(create_time__range=(today_min,
# today_max),member_type=0))

#     def get_descendant_count(self,member):
#         return len(member.get_descendants().filter(member_type=0))

#     def get_downline_count(self,member):
#         return len(member.get_children())

#     def get_binary(self,member):
#         if len(member.get_children().filter(member_type=0)) < 2 :
#             return False
#         else:
#             return True

#     def save(self):
#         if 'avatar_base64' in self.validated_data:
#             avatar = self.validated_data.pop('avatar_base64')
#             if len(avatar) > 0:
#                 avatar_base64 = avatar.split(',')[1]
#                 avatar_mime = avatar.split(';')[0].split(':')[1]
#                 avatar_extension = avatar_mime.split('/')[1]
#                 self.avatar = SimpleUploadedFile(name=str(uuid.uuid4())+'.'+avatar_extension, content=base64.b64decode(avatar_base64), content_type=avatar_mime)
#         super(MemberSerializer, self).save()

#     class Meta:
#         model = Member
# fields =
# ("id","descendant_count","today_descendant_count","binary","downline_count","member_type","user","avatar_base64",'quickblox_id','parent','downlines','create_time','external_id','name','points','avatar','phone','gender','postal_code','city','state','address','address_number','dream1','dream2','status','level','answers','birthday')


class MemberLoginSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    level = LevelSerializer(many=False, read_only=True)
    answers = serializers.SerializerMethodField()
    parent = UplineSerializer(many=False, read_only=True)
    downlines = serializers.SerializerMethodField(read_only=True)
    descendant_count = serializers.SerializerMethodField()
    downline_count = serializers.SerializerMethodField()
    binary = serializers.SerializerMethodField()
    today_descendant_count = serializers.SerializerMethodField()

    def get_downlines(self, obj):
        user = self.context['request'].user
        downlines = Member.objects.filter(parent=obj, member_type=0)
        # downlines = obj.get_descendants()
        print downlines
        serializer = DownlineSerializer(downlines, many=True)
        return serializer.data

    def get_answers(self, member):
        answers = MemberTrainingStep.objects.select_related(
            'training_step').filter(member=member)
        ret = []
        for answer in answers:
            ret.append(answer.training_step.id)
        return ret

    def get_descendant_count(self, member):
        return len(member.get_descendants().filter(member_type=0))

    def get_today_descendant_count(self, member):
        today_min = datetime.datetime.combine(
            datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(
            datetime.date.today(), datetime.time.max)
        return len(member.get_descendants().filter(create_time__range=(today_min, today_max), member_type=0))

    def get_downline_count(self, member):
        return len(member.get_children())

    def get_binary(self, member):
        if len(member.get_children().filter(member_type=0)) < 2:
            return False
        else:
            return True

    class Meta:
        model = Member
        fields = ("id", "descendant_count", "today_descendant_count", "binary", "downline_count", "member_type", 'user', 'member_uid', 'quickblox_id', 'quickblox_password', 'parent', 'downlines', 'create_time',
                  'external_id', 'name', 'points', 'avatar', 'phone', 'gender', 'postal_code', 'city', 'state', 'address', 'address_number', 'dream1', 'dream2', 'status', 'level', 'birthday', 'answers')


class ContactSerializer(BulkSerializerMixin, serializers.HyperlinkedModelSerializer):
    member = MemberSerializer(read_only=True)
    avatar_base64 = serializers.CharField(
        write_only=True, required=False, allow_blank=True)

    list_serializer_class = BulkListSerializer

    def create(self, validated_data):
        contact = Contact()
        member = Member.objects.get(user=self.context['request'].user)
        contact.owner = member

        if 'avatar_base64' in validated_data:
            avatar = validated_data.pop('avatar_base64')
            if len(avatar) > 0:
                avatar_base64 = avatar.split(',')[1]
                avatar_mime = avatar.split(';')[0].split(':')[1]
                avatar_extension = avatar_mime.split('/')[1]
                contact.avatar = SimpleUploadedFile(name=str(uuid.uuid4(
                )) + '.' + avatar_extension, content=base64.b64decode(avatar_base64), content_type=avatar_mime)

        if 'email' in validated_data:
            contact.email = validated_data.pop('email')
        if 'cellphone' in validated_data:
            contact.cellphone = validated_data.pop('cellphone')
        if 'birthday' in validated_data:
            contact.birthday = validated_data.pop('birthday')
        if 'cpf' in validated_data:
            contact.cpf = validated_data.pop('cpf')
        if 'rg' in validated_data:
            contact.rg = validated_data.pop('rg')
        if 'region' in validated_data:
            contact.region = validated_data.pop('region')
        if 'contact_category' in validated_data:
            contact.contact_category = validated_data.pop('contact_category')
        if 'name' in validated_data:
            contact.name = validated_data.pop('name')
        if 'phone' in validated_data:
            contact.phone = validated_data.pop('phone')
        if 'gender' in validated_data:
            contact.gender = validated_data.pop('gender')
        if 'postal_code' in validated_data:
            contact.postal_code = validated_data.pop('postal_code')
        if 'city' in validated_data:
            contact.city = validated_data.pop('city')
        if 'state' in validated_data:
            contact.state = validated_data.pop('state')
        if 'address' in validated_data:
            contact.address = validated_data.pop('address')
        contact.save()
        return contact

    class Meta:
        model = Contact
        fields = ("id", "avatar_base64", "avatar", "email", "cellphone", "birthday", "cpf", "rg", "region",
                  'member', 'contact_category', 'name', 'phone', 'gender', 'postal_code', 'city', 'state', 'address')


class ContactDownlineSerializer(serializers.HyperlinkedModelSerializer):
    member = DownlineSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = ("id", "avatar", "email", "cellphone", "birthday", "cpf", "rg", "region", 'member',
                  'contact_category', 'name', 'phone', 'gender', 'postal_code', 'city', 'state', 'address')


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ("id", "name", "active", "points",
                  "table_value", "create_time")


class SaleItemSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = SaleItem
        fields = ("id", "product", "quantity", "total", "notificate_at")


class SaleItemRegisterSerializer(serializers.HyperlinkedModelSerializer):
    sale = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Sale.objects.all(), write_only=True)
    product = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Product.objects.all())

    class Meta:
        model = SaleItem
        fields = ("id", "product", "quantity", "notificate_at", "sale")


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    client = ContactDownlineSerializer(read_only=True)
    sale_items = SaleItemSerializer(many=True, read_only=True)

    class Meta:
        model = Sale
        fields = ("id", "client", "sale_items", "active", "total",
                  "points", "create_time", "status", "send_time")


class SaleRegisterSerializer(serializers.HyperlinkedModelSerializer):
    client_id = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Contact.objects.all(), source="client")
    sale_items = SaleItemRegisterSerializer(many=True)

    class Meta:
        model = Sale
        fields = ("id", "client_id", "sale_items")


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', "user", "title", "content", "media",
                  "thumbnail", "media_type", "create_time", "update_time")


class CalendarSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Calendar
        fields = ("id", "name", "color")


class EventSerializer(serializers.HyperlinkedModelSerializer):
    invited = ContactSerializer(many=True, read_only=True)
    members = DownlineSerializer(many=True, read_only=True)
    invited_members = DownlineSerializer(
        many=True, read_only=True, required=False)
    calendar = CalendarSerializer(read_only=True)
    deleted = serializers.SerializerMethodField()
    inviter = UplineSerializer(many=False, read_only=True)
    begin_time = UTCDateTimeField()
    end_time = UTCDateTimeField()

    def transform_begin_time(self, instance):
        return 'batata'

    def get_deleted(self, instance):
        return False

    class Meta:
        model = Event
        fields = ("id", "is_invited", "invited_members", "inviter", "deleted", "alert_at_hour", "alert_5_mins", "alert_15_mins", "alert_30_mins", "alert_1_hour", "alert_2_hours", "alert_1_day",
                  "title", "all_day", "begin_time", "end_time", "invited", "members", "calendar", "note", "postal_code", "complement", "lat", "lng", 'state', 'city', 'address', 'address_number')


class EventDeleteSerializer(serializers.HyperlinkedModelSerializer):
    calendar = CalendarSerializer(read_only=True)
    deleted = serializers.SerializerMethodField()
    inviter = UplineSerializer(many=False, read_only=True)

    def get_deleted(self, instance):
        return True

    class Meta:
        model = Event
        fields = ("id", "is_invited", "inviter", "deleted", "alert_at_hour", "alert_5_mins", "alert_15_mins", "alert_30_mins", "alert_1_hour", "alert_2_hours", "alert_1_day",
                  "title", "all_day", "begin_time", "end_time", "calendar", "note", "postal_code", "complement", "lat", "lng", 'state', 'city', 'address', 'address_number')


class EventRegisterSerializer(serializers.HyperlinkedModelSerializer):
    invited = ContactSerializer(read_only=True, many=True)
    members = DownlineSerializer(read_only=True, many=True)
    invited_members = DownlineSerializer(
        read_only=True, many=True)
    invited_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Contact.objects.all(), write_only=True, source="invited")
    member_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Member.objects.all(), write_only=True, source="members")
    invited_member_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Member.objects.all(), required=False, write_only=True, source="invited_members")
    calendar_id = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Calendar.objects.all(), source='calendar')

    def update(self, instance, validated_data):
        event = instance
        if 'owner' in validated_data:
            event.owner = validated_data['owner']
        if 'title' in validated_data:
            event.title = validated_data['title']
        if 'all_day' in validated_data:
            event.all_day = validated_data['all_day']
        if 'begin_time' in validated_data:
            event.begin_time = validated_data['begin_time']
        if 'end_time' in validated_data:
            event.end_time = validated_data['end_time']
        if 'calendar' in validated_data:
            event.calendar = validated_data['calendar']
        if 'note' in validated_data:
            event.note = validated_data['note']
        if 'postal_code' in validated_data:
            event.postal_code = validated_data['postal_code']
        if 'region' in validated_data:
            event.region = validated_data['region']
        if 'city' in validated_data:
            event.city = validated_data['city']
        if 'state' in validated_data:
            event.state = validated_data['state']
        if 'address' in validated_data:
            event.address = validated_data['address']
        if 'address_number' in validated_data:
            event.address_number = validated_data['address_number']
        if 'complement' in validated_data:
            event.complement = validated_data['complement']
        if 'lat' in validated_data:
            event.lat = validated_data['lat']
        if 'lng' in validated_data:
            event.lng = validated_data['lng']
        if 'alert_at_hour' in validated_data:
            event.alert_at_hour = validated_data['alert_at_hour']
        if 'alert_5_mins' in validated_data:
            event.alert_5_mins = validated_data['alert_5_mins']
        if 'alert_15_mins' in validated_data:
            event.alert_15_mins = validated_data['alert_15_mins']
        if 'alert_30_mins' in validated_data:
            event.alert_30_mins = validated_data['alert_30_mins']
        if 'alert_1_hour' in validated_data:
            event.alert_1_hour = validated_data['alert_1_hour']
        if 'alert_2_hours' in validated_data:
            event.alert_2_hours = validated_data['alert_2_hours']
        if 'alert_1_day' in validated_data:
            event.alert_1_day = validated_data['alert_1_day']
        if 'parent_event' in validated_data:
            event.parent_event = validated_data['parent_event']
        if 'is_invited' in validated_data:
            event.is_invited = validated_data['is_invited']
        if 'inviter' in validated_data:
            event.inviter = validated_data['inviter']
        if 'invited' in validated_data:
            event.invited = validated_data['invited']
        if 'members' in validated_data:
            event.members = validated_data['members']
        if 'invited_members' in validated_data:
            event.invited_members = validated_data['invited_members']
        event.save()
        return event

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        print validated_data
        event = Event()
        if 'owner' in validated_data:
            event.owner = validated_data['owner']
        if 'title' in validated_data:
            event.title = validated_data['title']
        if 'all_day' in validated_data:
            event.all_day = validated_data['all_day']
        if 'begin_time' in validated_data:
            event.begin_time = validated_data['begin_time']
        if 'end_time' in validated_data:
            event.end_time = validated_data['end_time']
        if 'calendar' in validated_data:
            event.calendar = validated_data['calendar']
        if 'note' in validated_data:
            event.note = validated_data['note']
        if 'postal_code' in validated_data:
            event.postal_code = validated_data['postal_code']
        if 'region' in validated_data:
            event.region = validated_data['region']
        if 'city' in validated_data:
            event.city = validated_data['city']
        if 'state' in validated_data:
            event.state = validated_data['state']
        if 'address' in validated_data:
            event.address = validated_data['address']
        if 'address_number' in validated_data:
            event.address_number = validated_data['address_number']
        if 'complement' in validated_data:
            event.complement = validated_data['complement']
        if 'lat' in validated_data:
            event.lat = validated_data['lat']
        if 'lng' in validated_data:
            event.lng = validated_data['lng']
        if 'alert_at_hour' in validated_data:
            event.alert_at_hour = validated_data['alert_at_hour']
        if 'alert_5_mins' in validated_data:
            event.alert_5_mins = validated_data['alert_5_mins']
        if 'alert_15_mins' in validated_data:
            event.alert_15_mins = validated_data['alert_15_mins']
        if 'alert_30_mins' in validated_data:
            event.alert_30_mins = validated_data['alert_30_mins']
        if 'alert_1_hour' in validated_data:
            event.alert_1_hour = validated_data['alert_1_hour']
        if 'alert_2_hours' in validated_data:
            event.alert_2_hours = validated_data['alert_2_hours']
        if 'alert_1_day' in validated_data:
            event.alert_1_day = validated_data['alert_1_day']
        if 'parent_event' in validated_data:
            event.parent_event = validated_data['parent_event']
        if 'is_invited' in validated_data:
            event.is_invited = validated_data['is_invited']
        if 'inviter' in validated_data:
            event.inviter = validated_data['inviter']
        event.save()
        if 'invited' in validated_data:
            event.invited = validated_data['invited']
        if 'members' in validated_data:
            event.members = validated_data['members']
        if 'invited_members' in validated_data:
            event.invited_members = validated_data['invited_members']
        return event
        # return super(EventRegisterSerializer, self).create(validated_data)

    class Meta:
        model = Event
        fields = ("id", "alert_at_hour", "invited_ids", "invited", "alert_5_mins", "alert_15_mins", "alert_30_mins", "alert_1_hour", "alert_2_hours", "alert_1_day", "title", "all_day",
                  "begin_time", "end_time", "member_ids", "members", "invited_member_ids", "invited_members", "calendar_id", "note", "postal_code", "complement", "lat", "lng", 'state', 'city', 'address', 'address_number')


class StateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = State
        fields = ("id", "acronym", "name")


class CitySerializer(serializers.HyperlinkedModelSerializer):
    state = StateSerializer(many=False)

    class Meta:
        model = State
        fields = ("id", "state", "name")


class PostalCodeSerializer(serializers.HyperlinkedModelSerializer):
    city = CitySerializer(many=False)

    class Meta:
        model = PostalCode
        fields = ("city", "street", "neighborhood",
                  "postal_code", "street_type")


class GoalSerializer(serializers.HyperlinkedModelSerializer):
    level = LevelSerializer(many=False, read_only=True)
    level_id = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Level.objects.all(), write_only=True, source="level")

    def create(self, validated_data):
        goal = Goal()
        goal.level = validated_data.pop('level_id')
        member = Member.objects.get(user=self.context['request'].user)
        goal.member = member
        goal.date = validated_data.pop('date')
        goal.save()
        return goal

    class Meta:
        model = Goal
        fields = ("id", "level", "level_id", "date")


class MediaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Media
        fields = ("id", "name", "media", "thumbnail", "media_type")


class MediaCategorySerializer(serializers.HyperlinkedModelSerializer):
    medias = MediaSerializer(many=True, read_only=True)

    class Meta:
        model = MediaCategory
        fields = ("id", "name", "medias")


class InviteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Invite
        fields = ("id", "name", "email")

    def create(self, validated_data):
        validated_data['member'] = Member.objects.get(
            user=self.context['request'].user)
        return super(InviteSerializer, self).create(validated_data)
