# -*- coding: utf-8 -*-
import datetime
from django.contrib import admin
from django.utils.translation import ugettext as _
from upline.models import *
from upline.forms import *
from django_mptt_admin.admin import DjangoMpttAdmin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from django.contrib.admin import SimpleListFilter
from upline.quickblox import delete_user
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from solo.admin import SingletonModelAdmin
from upline.serializers import *


class TrainingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'notified']
    search_fields = ['name']
    actions = ['send']

    def send(modeladmin, request, queryset):
        for instance in queryset:
            devices = GCMDevice.objects.filter()
            if len(devices) > 0:
                devices.send_message(SiteConfiguration.get_solo().new_training_message, extra={
                                     "type": "training", "object": OnlyTrainingSerializer(instance, many=False, context={'request': request}).data})
        queryset.update(notified=True)

    send.short_description = u"Enviar notificações"


class LevelAdmin(admin.ModelAdmin):
    form = LevelForm
    list_display = ['id', 'title', 'points_range_from', 'points_range_to']
    search_fields = ['title']


class MemberAdmin(ForeignKeyAutocompleteAdmin, DjangoMpttAdmin):
    form = MemberForm
    list_display = ['id', "user", "parent", "name",
                    "points", "phone", "gender", "level", "get_acoes"]
    list_display_links = ['id']
    search_fields = ["name"]
    # actions = ['delete_model']
    related_search_fields = {
        'user': ['first_name', 'email'],
        'parent': ['name'],
    }

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(MemberAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_queryset(self, request):
        qs = super(MemberAdmin, self).get_queryset(request)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs.filter(member_type=0)

    def get_related_filter(self, model, request):
        if not issubclass(model, Member):
            return super(MemberAdmin, self).get_related_filter(
                model, request
            )
        return Q(member_type=0)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('quickblox_id',)
        return self.readonly_fields

    def get_acoes(self, obj):
        return '<a href="/upline/member/' + str(obj.id) + '/linear/">linear</a> <a href="/upline/member/' + str(obj.id) + '/binary/">binário</a> <a href="/upline/member/' + str(obj.id) + '/">editar</a>'

    get_acoes.short_description = 'Ações'
    get_acoes.allow_tags = True


class Invited(Member):

    class Meta:
        proxy = True


class InvitedAdmin(admin.ModelAdmin):
    form = MemberForm
    list_display = ['id', "user", "parent",
                    "name", "points", "phone", "gender"]
    list_display_links = ['id']
    search_fields = ['name']
    actions = ['delete_model', 'convert_to_member']
    related_search_fields = {
        'user': ('first_name', 'email'),
        'parent': ('name'),
    }

    def get_actions(self, request):
        actions = super(InvitedAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def convert_to_member(modeladmin, request, queryset):
        for obj in queryset:
            obj.member_type = 0
            obj.save()

    def delete_model(modeladmin, request, queryset):
        for obj in queryset:
            delete_user(obj)
            obj.user.delete()
            obj.delete()

    def get_queryset(self, request):
        qs = super(InvitedAdmin, self).get_queryset(request)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs.filter(member_type=1)

    def get_related_filter(self, model, request):
        if not issubclass(model, Member):
            return super(MemberAdmin, self).get_related_filter(
                model, request
            )
        return Q(member_type=0)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('quickblox_id',)
        return self.readonly_fields


class ContactAdmin(ForeignKeyAutocompleteAdmin):
    list_display = ['id', "owner", "name", "state", "city", "phone", "member"]
    list_display_links = ['id']
    search_fields = ['name']

    related_search_fields = {
        'owner': ('name'),
        'member': ('name'),
    }

    def get_related_filter(self, model, request):
        if not issubclass(model, Member):
            return super(ContactAdmin, self).get_related_filter(
                model, request
            )
        return Q(member_type=0)

    def get_queryset(self, request):
        qs = super(ContactAdmin, self).get_queryset(request)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs.filter(contact_category=0)


class Client(Contact):

    class Meta:
        proxy = True


class SaleInline(admin.TabularInline):
    model = Sale

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        return list(set(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]
        ))


class ClientAdmin(ForeignKeyAutocompleteAdmin):
    list_display = ['id', "owner", "name", "state", "city", "phone", "member"]
    list_display_links = ['id']
    search_fields = ['name']

    inlines = [
        SaleInline,
    ]

    related_search_fields = {
        'owner': ('name'),
        'member': ('name'),
    }

    def get_related_filter(self, model, request):
        if not issubclass(model, Member):
            return super(ClientAdmin, self).get_related_filter(
                model, request
            )
        return Q(member_type=0)

    def get_queryset(self, request):
        qs = super(ClientAdmin, self).get_queryset(request)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs.filter(contact_category=1)


class GoalAdmin(ForeignKeyAutocompleteAdmin):
    related_search_fields = {
        'member': ('name'),
    }

    def get_related_filter(self, model, request):
        if not issubclass(model, Member):
            return super(GoalAdmin, self).get_related_filter(
                model, request
            )
        return Q(member_type=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'points', 'table_value']


class SaleItemInline(admin.TabularInline):
    model = SaleItem

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        return list(set(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]
        ))


class SaleAdmin(ForeignKeyAutocompleteAdmin):
    list_display = ['id', 'member', 'client', 'create_time', 'total']

    inlines = [
        SaleItemInline,
    ]

    related_search_fields = {
        'member': ('name'),
        'client': ('name'),
    }

    def get_related_filter(self, model, request):
        if not issubclass(model, Member):
            return super(SaleAdmin, self).get_related_filter(
                model, request
            )
        return Q(member_type=0)

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['readonly'] = True
        return super(SaleAdmin, self).change_view(request, object_id, extra_context=extra_context)

    def has_delete_permission(self, request, x=None):
        return False

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return list(set(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]
        ))


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'state', 'name']
    search_fields = ['name']
    list_filter = ['state']


class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'acronym', 'name']
    search_fields = ['acronym', 'name']


class PostalCodeAdmin(ForeignKeyAutocompleteAdmin):
    related_search_fields = {
        'city': ('name'),
    }
    list_display = ['id', 'get_state', 'city', 'postal_code']
    search_fields = ['postal_code', 'city']
    list_filter = ['city__state']

    def get_state(self, obj):
        return obj.city.state

    get_state.short_description = 'State'
    get_state.admin_order_field = 'city__state'


class EventDateFilter(SimpleListFilter):
    title = _('Data')
    parameter_name = 'begin_time'

    def lookups(self, request, model_admin):
        month_list = Event.objects.datetimes('begin_time', "month")
        ret = []
        for month in month_list:
            ret.append([month.strftime('%m/%Y'), month.strftime('%m/%Y')])
        return ret

    def queryset(self, request, queryset):
        if self.value() == 'PREVIOUS':
            return queryset.filter(begin_time__lte=datetime.datetime.now())
        else:
            return queryset.filter(begin_time__gte=datetime.datetime.now())


class EventAdmin(ForeignKeyAutocompleteAdmin):
    change_list_template = 'event_change_list.html'
    form = EventForm
    list_display = ["id", "title", "calendar", "begin_time"]
    search_fields = ['name', 'owner']
    # list_filter = [EventDateFilter]
    related_search_fields = {
        'owner': ['username'],
        'calendar': ['name'],
        'invited': ['name'],
        'members': ['name'],
    }

    def get_queryset(self, request):
        qs = super(EventAdmin, self).get_queryset(
            request).filter(is_invited=False)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        else:
            return qs

    def get_related_filter(self, model, request):
        if not issubclass(model, Member):
            return super(EventAdmin, self).get_related_filter(
                model, request
            )
        return Q(member_type=0)


class PostAdmin(ForeignKeyAutocompleteAdmin):
    list_display = ['user', 'title', 'content', 'create_time',
                    'media_type', 'get_media_file', 'notified']
    form = PostForm
    related_search_fields = {
        'user': ('first_name', 'email'),
    }
    actions = ['send']

    def send(modeladmin, request, queryset):
        for instance in queryset:
            devices = GCMDevice.objects.filter(
                user__groups__in=instance.groups.all())
            if len(devices) > 0:
                devices.send_message(SiteConfiguration.get_solo().new_post_message, extra={
                                     "type": "post", "object": PostSerializer(instance, many=False, context={'request': request}).data})
        queryset.update(notified=True)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('converted',)
        return self.readonly_fields

    def get_media_file(self, obj):
        if obj.media_type == 0:
            return u'<img src="' + unicode(obj.media) + '" style="width:300px"/>'
        elif obj.media_type == 1:
            return u'<audio src="' + unicode(obj.media) + '" controls>Your browser does not support the <code>audio</code> element.</audio>'
        elif obj.media_type == 2:
            return u'<video style="width:300px" controls><source src="' + unicode(obj.media) + '" type="video/mp4">Seu navegador nao suporta o elemento <code>video</code>.</video>'
        elif obj.media_type == 3:
            return ''
        else:
            return u'<a target="_blank" class="pdf" href="' + unicode(obj.media) + '">' + unicode(obj.name) + '</a>'

    get_media_file.short_description = 'Arquivo'
    get_media_file.allow_tags = True
    send.short_description = u"Enviar notificações"


class CalendarAdmin(ForeignKeyAutocompleteAdmin):
    related_search_fields = {
        'user': ('first_name', 'email'),
    }


class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_media_type', 'media_category',
                    'name', 'get_media_file', 'notified']
    search_fields = ['name']
    list_filter = ['media_type']
    actions = ['send']

    def send(modeladmin, request, queryset):
        for instance in queryset:
            devices = GCMDevice.objects.filter()
            if len(devices) > 0:
                devices.send_message(SiteConfiguration.get_solo().new_media_message, extra={
                                     "type": "media", "object": MediaSerializer(instance, many=False, context={'request': request}).data})
        queryset.update(notified=True)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('converted',)
        return self.readonly_fields

    def get_media_type(self, obj):
        return obj.get_media_type_display()

    def get_media_file(self, obj):
        if obj.media_type == 0:
            return u'<img src="' + obj.media + '" style="width:300px"/>'
        elif obj.media_type == 1:
            return u'<audio src="' + obj.media + '" controls>Your browser does not support the <code>audio</code> element.</audio>'
        elif obj.media_type == 2:
            return u'<video style="width:300px" controls><source src="' + unicode(obj.media) + '" type="video/mp4">Seu navegador nao suporta o elemento <code>video</code>.</video>'
        else:
            return u'<a target="_blank" class="pdf" href="' + obj.media + '">' + obj.name + '</a>'

    get_media_file.short_description = 'Arquivo'
    get_media_file.allow_tags = True
    get_media_type.short_description = 'Media Type'
    get_media_type.admin_order_field = 'media_category__media_type'
    send.short_description = u"Enviar notificações"


class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class TrainingStepAdmin(admin.ModelAdmin):
    list_display = ["step", "training", "title", "description"]
    search_fields = ['name']
    list_filter = ['training']
    form = TrainingStepForm

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('converted',)
        return self.readonly_fields


class InviteAdmin(admin.ModelAdmin):
    search_fields = ['member', 'name', 'email']
    list_display = ['id', 'member', 'name', 'email', 'create_time']
    change_list_template = 'admin/invite_list.html'

    def has_edit_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return list(set(
                [field.name for field in self.opts.local_fields] +
                [field.name for field in self.opts.local_many_to_many]
            ))
        return self.readonly_fields

    def get_actions(self, request):
        actions = super(InviteAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'level', 'message', 'sent', 'get_date_sent']
    actions = ['send']

    def get_date_sent(self, obj):
        if obj.sent:
            return obj.update_time
        else:
            return None

    get_date_sent.short_description = 'Data do Envio'

    def send(modeladmin, request, queryset):
        for notification in queryset:
            devices = GCMDevice.objects.filter(
                user__in=notification.level.user_set.all())
            devices.send_message(notification.message)
        queryset.update(sent=True)

    send.short_description = u"Enviar notificações"


class AvatarInline(admin.StackedInline):
    model = Avatar


class MyUserAdmin(UserAdmin):

    inlines = [
        AvatarInline,
    ]

    def get_actions(self, request):
        actions = super(MyUserAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        if obj:  # In edit mode
            return ('username',) + self.readonly_fields
        return self.readonly_fields

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        else:
            return False

admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Invite, InviteAdmin)
admin.site.register(Invited, InvitedAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(TrainingStep, TrainingStepAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(PostalCode, PostalCodeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(MediaCategory, MediaCategoryAdmin)
