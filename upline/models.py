# -*- coding: utf-8 -*-
# from upline.quickblox import create_user
import base64
import os
import uuid
from mimetypes import MimeTypes

from colorful.fields import RGBColorField
from Crypto.Cipher import AES
from django.conf import settings
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.core.validators import validate_email
from django.db import models
from django.db.models import Q
from django.db.models.signals import m2m_changed, post_save, pre_delete
from django.dispatch.dispatcher import receiver
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from mptt.models import MPTTModel, TreeForeignKey
from push_notifications.models import GCMDevice
from rq import Queue
from s3direct.fields import S3DirectField
from solo.models import SingletonModel
from utils import convert_media
from worker import conn


def avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join('image', filename)


def thumbnails_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join('image', filename)


def levels_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join('image', filename)


def members_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join('image', filename)


def dreams_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join('image', filename)


def answer_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join('image', filename)


def contacts_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join('image', filename)


class SiteConfiguration(SingletonModel):
    new_event_message = models.CharField(
        max_length=255, null=True, blank=True, default=None, verbose_name=_('new event message'))
    new_training_message = models.CharField(
        max_length=255, null=True, blank=True, default=None, verbose_name=_('new training message'))
    new_post_message = models.CharField(
        max_length=255, null=True, blank=True, default=None, verbose_name=_('new post message'))
    new_media_message = models.CharField(
        max_length=255, null=True, blank=True, default=None, verbose_name=_('new media message'))
    update_event_message = models.CharField(
        max_length=255, null=True, blank=True, default=None, verbose_name=_('update event message'))
    first_training = models.ForeignKey(
        "TrainingStep", null=True, blank=True, default=None)

    def __unicode__(self):
        return _("Configuration")

    class Meta:
        verbose_name = _("Configuration")


class Avatar(models.Model):
    user = models.OneToOneField(User, verbose_name=_('user'))
    image = models.ImageField(upload_to=avatar_path)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatar"


class State(models.Model):
    acronym = models.CharField(max_length=2, verbose_name=_('acronym'))
    name = models.CharField(max_length=255, verbose_name=_('name'))
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    class Meta:
        verbose_name = _('state')
        verbose_name_plural = _('states')

    def __unicode__(self):
        return self.acronym


class City(models.Model):
    state = models.ForeignKey(State, verbose_name=_('state'))
    name = models.CharField(max_length=255, verbose_name=_('name'))
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('citys')

    def __unicode__(self):
        return self.state.acronym + ' - ' + self.name

    def to_json(self):
        return {'state': self.state.acronym, 'name': self.name, 'id': self.id}


class PostalCode(models.Model):
    city = models.ForeignKey(City, verbose_name=_('city'))
    street = models.CharField(max_length=255, verbose_name=_('street'))
    neighborhood = models.CharField(
        max_length=255, verbose_name=_('neighborhood'))
    postal_code = models.CharField(
        max_length=255, verbose_name=_('postal_code'))
    street_type = models.CharField(
        max_length=255, verbose_name=_('street_type'))
    approved = models.BooleanField(default=False, verbose_name=_('approved'))
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    class Meta:
        verbose_name = _('postal code')
        verbose_name_plural = _('postal codes')

    def __unicode__(self):
        return self.postal_code

    def to_json(self):
        return {'city': self.city.name, 'state': self.city.state.acronym, 'street': '%s %s' % (self.street_type, self.street), 'zip_code': self.zip_code, 'neighborhood': self.neighborhood}


class Training(models.Model):
    position = models.IntegerField(default=99999, verbose_name=_('position'))
    name = models.CharField(max_length=255, verbose_name=_('name'))
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))
    notified = models.BooleanField(default=False, editable=False)
    have_notifications = models.BooleanField(default=False)
    previous_training = models.ForeignKey('Training', verbose_name=_(
        'previous training'), null=True, blank=True, default=None)
    day_1_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_1_notification_description'))
    day_2_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_2_notification_description'))
    day_3_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_3_notification_description'))
    day_4_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_4_notification_description'))
    day_5_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_5_notification_description'))
    day_6_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_6_notification_description'))
    day_7_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_7_notification_description'))
    day_14_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_14_notification_description'))
    day_28_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_28_notification_description'))

    class Meta:
        verbose_name = _("training")
        verbose_name_plural = _("trainings")
        ordering = ['position']

    def __unicode__(self):
        return self.name


class TrainingStep(models.Model):
    training = models.ForeignKey(
        Training, related_name='training_steps', verbose_name=_('training'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    media = S3DirectField(dest='training_steps', null=True, blank=True)
    media_type = models.IntegerField(choices=((0, 'Imagem'), (1, 'Audio'), (
        2, 'Video'), (3, 'Texto')), verbose_name=_('media_type'), default=0, editable=False)
    thumbnail = models.ImageField(
        upload_to=thumbnails_path, blank=True, null=True, verbose_name=_('thumbnail'), editable=True)
    converted = models.BooleanField(default=False)
    step = models.IntegerField(verbose_name=_('step'))
    description = models.TextField(
        blank=True, null=True, verbose_name=_('description'))
    need_answer = models.BooleanField(
        default=False, verbose_name=_('need_answer'))
    answer_type = models.IntegerField(verbose_name=_('answer_type'), choices=((0, _('text')), (1, _(
        'audio')), (2, _('video')), (5, _('image')), (3, _('list')), (4, _('meeting'))), null=True, default=None)
    meetings_per_week = models.IntegerField(
        blank=True, null=True, verbose_name=_('meetings_per_week'))
    weeks = models.IntegerField(blank=True, null=True, verbose_name=_('weeks'))
    nr_contacts = models.IntegerField(
        blank=True, null=True, verbose_name=_('nr_contacts'))
    have_notifications = models.BooleanField(default=False)
    day_1_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_1_notification_description'))
    day_2_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_2_notification_description'))
    day_3_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_3_notification_description'))
    day_4_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_4_notification_description'))
    day_5_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_5_notification_description'))
    day_6_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_6_notification_description'))
    day_7_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_7_notification_description'))
    day_14_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_14_notification_description'))
    day_28_notification_description = models.TextField(
        blank=True, null=True, verbose_name=_('day_28_notification_description'))
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    class Meta:
        verbose_name = _("training step")
        verbose_name_plural = _("training steps")
        ordering = ['step']

    def __unicode__(self):
        return self.title

    def next_training_step(self):
        training_steps = TrainingStep.objects.filter(Q(training=self.training, step__gt=self.step) | Q(
            training__position__gt=self.training.position)).order_by("training__position", "step")
        if len(training_steps) > 0:
            return training_steps[0]
        return None

    def send_notification(self):
        self.save()
        from upline.serializers import TrainingStepTaskSerializer
        devices = GCMDevice.objects.all()
        if len(devices) > 0:
            devices.send_message(SiteConfiguration.get_solo().new_training_message, extra={
                "type": "training_step", "object": TrainingStepTaskSerializer(self, many=False).data})
        self.notified = True
        self.save()

    def save(self, *args, **kwargs):
        if self.media and len(self.media) > 3:
            mime = MimeTypes()
            mime_type = mime.guess_type(self.media)
            if mime_type[0] is not None:
                t = mime_type[0].split('/')[0]

                if t == 'image':
                    self.media_type = 0
                elif t == 'audio':
                    self.media_type = 1
                elif t == 'video':
                    self.media_type = 2
                else:
                    self.media_type = 3
            else:
                self.media_type = 3

        super(TrainingStep, self).save(*args, **kwargs)

        if not self.converted:
            q = Queue(connection=conn)
            q.enqueue(convert_media, self)


class Level(models.Model):
    title = models.CharField(
        unique=True, max_length=255, verbose_name=_('title'))
    image = models.ImageField(null=True, blank=True,
                              upload_to=levels_path, verbose_name=_('image'))
    color = RGBColorField(default="#ffffff")
    description = models.TextField(null=True, verbose_name=_('description'))
    gift = models.TextField(null=True, verbose_name=_('gift'))
    group = models.ForeignKey(Group, verbose_name=_(
        'group'), null=True, editable=False)
    points_range_from = models.IntegerField(
        verbose_name=_('points_range_from'))
    points_range_to = models.IntegerField(verbose_name=_('points_range_to'))
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    def save(self, *args, **kwargs):
        if not self.pk:
            group = Group()
            group.name = self.title
            group.save()
            self.group = group
        else:
            self.group.name = self.title
            self.group.save()
        super(Level, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("level")
        verbose_name_plural = _("levels")
        ordering = ['points_range_to']

    def __unicode__(self):
        return self.title


class Binary(MPTTModel):
    member = models.ForeignKey('Member')
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='downlines', db_index=True, verbose_name=_('parent'))
    node_position = models.IntegerField(default=0)
    can_left = models.BooleanField(default=False)
    can_right = models.BooleanField(default=False)

    def get_binary(self, level=None):
        if level is None:
            level = self.get_level()

        ret = {'obj': self, 'left': None, 'right': None}
        if self.get_level() < level + 3:
            left = self.get_children().filter(node_position=0)
            if len(left) > 0:
                ret['left'] = left[0].get_binary(level)
            right = self.get_children().filter(node_position=1)
            if len(right) > 0:
                ret['right'] = right[0].get_binary(level)
        return ret


class Member(MPTTModel):
    member_uid = models.UUIDField(unique=True, null=True, editable=False)
    member_type = models.IntegerField(default=0, choices=(
        (0, 'Membro'), (1, 'Convidado')), editable=False)
    user = models.OneToOneField(User, verbose_name=_('user'))
    email = models.EmailField(max_length=255, null=True, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='downlines', db_index=True, verbose_name=_('parent'))
    external_id = models.IntegerField(
        unique=True, blank=True, null=True, verbose_name=_('external_id'))
    name = models.CharField(max_length=50, verbose_name=_('name'))
    quickblox_id = models.CharField(
        max_length=255, null=True, verbose_name=_('quickblox_id'), editable=False)
    quickblox_password = models.CharField(
        max_length=255, null=True, verbose_name=_('quickblox_password'), editable=False)
    points = models.IntegerField(default=0, verbose_name=_('points'))
    avatar = models.ImageField(
        upload_to=members_path, blank=True, null=True, verbose_name=_('avatar'))
    phone = models.CharField(max_length=45, blank=True,
                             null=True, verbose_name=_('phone'))
    gender = models.IntegerField(
        choices=((0, "Masculino"), (1, 'Feminino')), verbose_name=_('gender'))
    postal_code = models.CharField(
        max_length=255, verbose_name=_('postal_code'))
    city = models.CharField(max_length=255, blank=True,
                            null=True, verbose_name=_('city'))
    state = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name=_('state'))
    address = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_('address'))
    address_number = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_('address_number'))
    dream1 = models.ImageField(
        upload_to=dreams_path, blank=True, null=True, default=None, verbose_name=_('dream1'))
    dream2 = models.ImageField(
        upload_to=dreams_path, blank=True, null=True, default=None, verbose_name=_('dream2'))
    status = models.CharField(blank=True, null=True,
                              verbose_name=_('status'), max_length=255)
    birthday = models.DateField(null=True, verbose_name=_('birthday'))
    level = models.ForeignKey(Level, verbose_name=_(
        'level'), editable=False, default=1)
    outpooring = models.IntegerField(default=0, verbose_name=_(
        'outpooring'), choices=((0, 'Esquerda'), (1, 'Direita')))
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    all_items = []

    def nr_invided(self):
        return Invite.objects.filter(member=self).count()

    def nr_contacts(self):
        return Contact.objects.filter(owner=self, contact_category=0).count()

    def nr_clients(self):
        return Contact.objects.filter(owner=self, contact_category=1).count()

    def get_binary(self):
        binary = Binary.objects.filter(member=self)
        if len(binary) > 0:
            return binary[0].get_binary()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.member_uid = str(uuid.uuid4())
            # self.quickblox_password = User.objects.make_random_password()
            # self = create_user(self)
            # self.encrypt_quickblox_password()
        # else:
            # self = update_user(self)
        level = Level.objects.filter(
            points_range_from__lte=self.points, points_range_to__gte=self.points)
        if len(level) > 0:
            self.user.groups.remove(self.level.group)
            self.level = level[0]
            self.user.groups.add(self.level.group)
            self.user.save()
        if self.email:
            self.user.email = self.email
            self.user.save()
        super(Member, self).save(*args, **kwargs)
        # if len(Binary.objects.filter(member=self)) == 0:
        #     Binary.create_member(self)

    class Meta:
        verbose_name = _("member")
        verbose_name_plural = _("members")

    class MPTTMeta:
        order_insertion_by = ['name']
        level_attr = 'mptt_level'

    def __unicode__(self):
        return self.name

    def encrypt_quickblox_password(self):
        key = "%s%s%s" % (self.user.username, str(
            self.quickblox_id), self.member_uid)
        enc_secret = AES.new(key[:32])
        tag_string = (str(self.quickblox_password) +
                      (AES.block_size -
                       len(str(self.quickblox_password)) % AES.block_size) * "\0")
        cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))
        self.quickblox_password = cipher_text

    def decrypted_quickblox_password(self):
        key = "%s%s%s" % (self.user.username, str(
            self.quickblox_id), self.member_uid)
        dec_secret = AES.new(key[:32])
        raw_decrypted = dec_secret.decrypt(
            base64.b64decode(self.quickblox_password))
        clear_val = raw_decrypted.rstrip("\0")
        return clear_val


class MemberTrainingStep(models.Model):
    member = models.ForeignKey(
        Member, related_name='answers', verbose_name=_('member'))
    training_step = models.ForeignKey(
        TrainingStep, related_name='members', verbose_name=_('training_step'))
    answer = models.TextField(verbose_name=_('answer'))
    media = models.FileField(upload_to=answer_path,
                             null=True, blank=True, default=None)
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    class Meta:
        verbose_name = _("member traing step")
        verbose_name_plural = _("member traing steps")

    def __unicode__(self):
        return self.member.name + ' - ' + self.training_step.title


class Contact(models.Model):
    owner = models.ForeignKey(
        Member, related_name="contact_owner", verbose_name=_('upline'))
    member = models.ForeignKey(
        Member, related_name="contact_member", blank=True, null=True, verbose_name=_('member'))
    avatar = models.ImageField(
        upload_to=contacts_path, blank=True, null=True, verbose_name=_('avatar'))
    contact_category = models.IntegerField(
        choices=((0, 'Contato'), (1, 'Cliente')), verbose_name=_('contact_category'))
    gender = models.IntegerField(choices=((-1, "-"), (0, "Masculino"), (1, 'Feminino')),
                                 verbose_name=_('gender'), null=True, blank=True, default=-1)
    name = models.CharField(max_length=255, verbose_name=_('name'))
    email = models.EmailField(
        max_length=255, null=True, verbose_name=_('email'), blank=True)
    phone = models.CharField(max_length=45, blank=True,
                             null=True, verbose_name=_('phone'))
    cellphone = models.CharField(
        max_length=45, blank=True, null=True, verbose_name=_('cellphone'))
    birthday = models.DateField(null=True, verbose_name=_(
        'birthday'), blank=True, default=None)
    cpf = models.CharField(max_length=45, blank=True,
                           null=True, verbose_name=_('cpf'))
    rg = models.CharField(max_length=45, blank=True,
                          null=True, verbose_name=_('rg'))
    postal_code = models.CharField(max_length=255, verbose_name=_(
        'postal_code'), null=True, blank=True)
    region = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_('region'))
    city = models.CharField(max_length=255, blank=True,
                            null=True, verbose_name=_('city'))
    state = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name=_('state'))
    address = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_('address'))
    address_number = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_('address_number'))
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Goal(models.Model):
    member = models.ForeignKey(Member, verbose_name=_('member'))
    level = models.ForeignKey(Level, verbose_name=_('level'))
    date = models.DateTimeField(verbose_name=_('date'))
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    class Meta:
        verbose_name = _("goal")
        verbose_name_plural = _("goals")

    def __unicode__(self):
        return self.level.title + " - " + self.member.name


class LogMemberLogin(models.Model):
    member = models.ForeignKey(Member, verbose_name=_('member'))
    ipv4_address = models.CharField(
        max_length=15, blank=True, null=True, verbose_name=_('ipv4_address'))
    ipv6_address = models.CharField(
        max_length=40, blank=True, null=True, verbose_name=_('ipv6_address'))
    agent = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name=_('agent'))
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    class Meta:
        verbose_name = _("log member login")
        verbose_name_plural = _("log member logins")

    def __unicode__(self):
        return self.member.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    active = models.BooleanField(default=True, verbose_name=_('active'))
    points = models.IntegerField(default=0, verbose_name=_('points'))
    table_value = models.DecimalField(
        max_digits=11, decimal_places=2, verbose_name=_('table_value'))
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __unicode__(self):
        return self.name


class Sale(models.Model):
    member = models.ForeignKey(Member, verbose_name=_('member'))
    external_id = models.IntegerField(null=True, blank=True, default=None)
    client = models.ForeignKey(Contact, verbose_name=_('client'))
    active = models.BooleanField(default=True, verbose_name=_('active'))
    total = models.DecimalField(
        max_digits=11, decimal_places=2, default="0.00", verbose_name=_('total'))
    points = models.IntegerField(default=0, verbose_name=_('points'))
    status = models.IntegerField(default=0, choices=(
        (0, 'Novo'), (1, 'Enviado'), (2, 'Aprovado'), (3, 'Cancelado')))
    pontuated = models.BooleanField(
        default=False, verbose_name=_('pontuated'), editable=False)
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))
    send_time = models.DateTimeField(null=True, verbose_name=_('send_time'))

    def save(self, *args, **kwargs):
        if self.status == 2 and not self.pontuated:
            self.member.points += self.points
            self.member.save()
        super(Sale, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("sale")
        verbose_name_plural = _("sales")
        ordering = ['-create_time']

    def __unicode__(self):
        return str(self.id)


class SaleItem(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('product'))
    sale = models.ForeignKey(
        Sale, related_name='sale_items', verbose_name=_('sale'))
    quantity = models.IntegerField(default=0, verbose_name=_('quantity'))
    total = models.DecimalField(
        max_digits=11, decimal_places=2, default="0.00", verbose_name=_('total'))
    notificate_at = models.DateField(verbose_name=_(
        'notificate_at'), null=True, blank=True, default=None)
    notified = models.BooleanField(default=False, verbose_name=_('notified'))
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    class Meta:
        verbose_name = _("sale item")
        verbose_name_plural = _("sale items")

    def __unicode__(self):
        return str(self.id)


class Post(models.Model):
    user = models.ForeignKey(
        User, related_name='posts', verbose_name=_('user'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    groups = models.ManyToManyField(
        Group, null=True, blank=True, default=None, verbose_name=_('groups'))
    content = models.TextField(
        null=True, blank=True, default=None, verbose_name=_('content'))
    media = S3DirectField(dest='posts', null=True, blank=True, default=None)
    media_type = models.IntegerField(choices=((0, 'Imagem'), (1, 'Audio'), (
        2, 'Video'), (3, 'Texto')), verbose_name=_('media_type'), default=0, editable=False)
    thumbnail = models.ImageField(
        upload_to=thumbnails_path, blank=True, null=True, verbose_name=_('thumbnail'), editable=True)
    converted = models.BooleanField(default=False)
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))
    notified = models.BooleanField(default=False, editable=False)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ['-create_time']

    def __unicode__(self):
        return self.title

    def send_notification(self):
        self.save()
        from upline.serializers import PostSerializer
        devices = GCMDevice.objects.filter(user__groups__in=self.groups.all())
        if len(devices) > 0:
            devices.send_message(SiteConfiguration.get_solo().new_post_message, extra={
                "type": "post", "object": PostSerializer(self, many=False).data})
        self.notified = True
        self.save()

    def save(self, *args, **kwargs):
        if self.media:
            mime = MimeTypes()
            mime_type = mime.guess_type(self.media)
            if mime_type[0] is not None:
                t = mime_type[0].split('/')[0]

                if t == 'image':
                    self.media_type = 0
                elif t == 'audio':
                    self.media_type = 1
                elif t == 'video':
                    self.media_type = 2
                else:
                    self.media_type = 3
            else:
                self.media_type = 3

        super(Post, self).save(*args, **kwargs)

        if not self.converted and self.media_type != 3:
            q = Queue(connection=conn)
            q.enqueue(convert_media, self)


class Calendar(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    color = RGBColorField(default="#ffffff")

    class Meta:
        verbose_name = _("calendar")
        verbose_name_plural = _("calendars")

    def __unicode__(self):
        return self.name


class Event(models.Model):
    owner = models.ForeignKey(User, verbose_name=_('owner'))
    groups = models.ManyToManyField(
        Group, null=True, blank=True, default=None, verbose_name=_('groups'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    all_day = models.BooleanField(default=False, verbose_name=_('all_day'))
    begin_time = models.DateTimeField(null=True, verbose_name=_('begin_time'))
    end_time = models.DateTimeField(null=True, verbose_name=_('end_time'))
    invited = models.ManyToManyField(
        Contact, blank=True, verbose_name=_('contacts'))
    members = models.ManyToManyField(
        Member, blank=True, verbose_name=_('members'))
    invited_members = models.ManyToManyField(Member, blank=True, verbose_name=_(
        'invited members'), related_name="invited_members")
    calendar = models.ForeignKey(
        Calendar, related_name='events', verbose_name=_('calendar'))
    note = models.TextField(null=True, blank=True, verbose_name=_('note'))
    postal_code = models.CharField(max_length=255, verbose_name=_(
        'postal_code'), null=True, blank=True)
    region = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_('region'))
    city = models.CharField(max_length=255, blank=True,
                            null=True, verbose_name=_('city'))
    state = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name=_('state'))
    address = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_('address'))
    address_number = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_('address_number'))
    complement = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_('complement'))
    lat = models.FloatField(null=True, blank=True,
                            default=None, verbose_name=_('lat'))
    lng = models.FloatField(null=True, blank=True,
                            default=None, verbose_name=_('lng'))
    alert_at_hour = models.BooleanField(default=False)
    alert_5_mins = models.BooleanField(default=False)
    alert_15_mins = models.BooleanField(default=False)
    alert_30_mins = models.BooleanField(default=False)
    alert_1_hour = models.BooleanField(default=False)
    alert_2_hours = models.BooleanField(default=False)
    alert_1_day = models.BooleanField(default=False)
    parent_event = models.ForeignKey(
        "Event", null=True, blank=True, default=None)
    is_invited = models.BooleanField(default=False)
    inviter = models.ForeignKey(Member, verbose_name=_(
        'inviter'), null=True, blank=True, related_name='Invited')

    def send_invite(self):
        for invited in self.invited.all():
            try:
                validate_email(invited.email)
                subject, from_email, to = 'Convite ' + \
                    settings.APPLICATION_NAME, settings.EMAIL_HOST_USER, invited.email
                text_content = render_to_string(
                    'event.txt', {'event': self, 'member': self.owner, 'name': invited.name})
                html_content = render_to_string(
                    'event.html', {'event': self, 'member': self.owner, 'name': invited.name})
                msg = EmailMultiAlternatives(
                    subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                print 'email sent'
            except ValidationError as e:
                print e
                print "oops! wrong email"

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")
        ordering = ['-begin_time']

    def __unicode__(self):
        return self.title


class EventAlert(models.Model):
    event = models.ForeignKey(Event)
    alert_date = models.DateTimeField(
        null=True, blank=True, default=None, verbose_name=_('alert_date'))

    class Meta:
        verbose_name = _("Event Alert")
        verbose_name_plural = _("Event Alerts")


class MediaCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))

    class Meta:
        verbose_name = _("media category")
        verbose_name_plural = _("media categorys")

    def __unicode__(self):
        return self.name


class Media(models.Model):
    media_type = models.IntegerField(choices=((0, 'Imagem'), (1, 'Audio'), (
        2, 'Video'), (3, 'PDF')), default=0, verbose_name=_('media_type'), editable=False)
    media_category = models.ForeignKey(
        MediaCategory, related_name='medias', verbose_name=_('media_category'))
    name = models.CharField(max_length=255, verbose_name=_('name'))
    media = S3DirectField(dest='media')
    thumbnail = models.ImageField(
        upload_to=thumbnails_path, blank=True, editable=True, null=True, verbose_name=_('thumbnail'))
    converted = models.BooleanField(default=False, editable=False)
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))
    notified = models.BooleanField(default=False, editable=False)

    def send_notification(self):
        self.save()
        from upline.serializers import MediaSerializer
        devices = GCMDevice.objects.all()
        if len(devices) > 0:
            devices.send_message(SiteConfiguration.get_solo().new_media_message, extra={
                "type": "media", "object": MediaSerializer(self, many=False).data})
        self.notified = True
        self.save()

    class Meta:
        verbose_name = _("media")
        verbose_name_plural = _("medias")

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.media:
            mime = MimeTypes()
            mime_type = mime.guess_type(self.media)

            t = mime_type[0].split('/')[0]

            if t == 'image':
                self.media_type = 0
            elif t == 'audio':
                self.media_type = 1
            elif t == 'video':
                self.media_type = 2
            else:
                self.media_type = 3

        super(Media, self).save(*args, **kwargs)

        if not self.converted:
            q = Queue(connection=conn)
            q.enqueue(convert_media, self)


class Notification(models.Model):
    level = models.ForeignKey(Group, verbose_name=_('level'))
    message = models.CharField(max_length=255, verbose_name=_(
        'message'), help_text=_('255 characters'))
    sent = models.BooleanField(
        default=False, editable=False, verbose_name=_('sent'))
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    def save(self, *args, **kwargs):
        super(Notification, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __unicode__(self):
        return self.message


class Invite(models.Model):
    member = models.ForeignKey(Member)
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255)
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name=_('create_time'))
    update_time = models.DateTimeField(
        auto_now=True, verbose_name=_('update_time'))

    def send_invite(self):
        subject, from_email, to = 'Convite ' + \
            settings.APPLICATION_NAME, settings.EMAIL_HOST_USER, self.email
        text_content = render_to_string('email.txt', {
                                        'app': settings.APPLICATION_NAME, 'member': self.member, 'name': self.name, 'link': settings.APPLICATION_URL})
        html_content = render_to_string('email.html', {
                                        'app': settings.APPLICATION_NAME, 'member': self.member, 'name': self.name, 'link': settings.APPLICATION_URL})
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def save(self, *args, **kwargs):
        self.send_invite()
        super(Invite, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Invite"
        verbose_name_plural = "Invites"

    def __unicode__(self):
        return self.email

from upline.serializers import EventDeleteSerializer, EventSerializer


def push_event(sender, instance, **kwargs):
    devices = GCMDevice.objects.filter(user=instance.owner)
    if len(devices) > 0:
        print "push_event"
        devices.send_message(SiteConfiguration.get_solo().new_event_message, extra={
                             "type": "event", "object": EventSerializer(instance, many=False).data})
    if len(instance.groups.all()) > 0 and not instance.is_invited:
        create_sub_events(instance)

post_save.connect(push_event, sender=Event, dispatch_uid="push_event")


def push_delete_event(sender, instance, **kwargs):
    devices = GCMDevice.objects.filter(user=instance.owner)
    if len(devices) > 0:
        devices.send_message(SiteConfiguration.get_solo().update_event_message, extra={
                             "type": "event", "object": EventDeleteSerializer(instance, many=False).data})

pre_delete.connect(push_delete_event, sender=Event, dispatch_uid="push_event")


@receiver(m2m_changed, sender=Event.invited.through)
def send_notifications_to_inviteds(sender, instance, action, **kwargs):
    if action == "post_add" and not instance.is_invited:
        instance.send_invite()


def create_sub_events(instance):
    print "create_sub_events"
    members = instance.members.all()
    invited_members = instance.invited_members.all()
    users = []
    for member in members:
        users.append(member.user)

    for member in invited_members:
        users.append(member.user)

    members = Member.objects.filter(level__group__in=instance.groups.all())
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
        e.inviter = Member.objects.get(user=instance.owner)
        e.save()

    for event in exclude_events:
        event.delete()

    for event in related_events:
        if event not in exclude_events:
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
            event.save()


@receiver(m2m_changed, sender=Event.members.through)
def send_notifications_to_members(sender, instance, action, **kwargs):
    if action == "post_add" and not instance.is_invited:
        create_sub_events(instance)


@receiver(m2m_changed, sender=Event.groups.through)
def send_notifications_to_groups(sender, instance, action, **kwargs):
    print "Event groups changed =>" + action
    if action == "post_add" and not instance.is_invited:
        create_sub_events(instance)
