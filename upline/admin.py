 # -*- coding: utf-8 -*-
import datetime
from django.contrib import admin
from django.utils.translation import ugettext as _
from upline.models import *
from upline.forms import *
from django_mptt_admin.admin import DjangoMpttAdmin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from django.conf import settings
from django.contrib.admin.util import flatten_fieldsets
from django.contrib.admin import SimpleListFilter
from upline.quickblox import create_user, delete_user
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']
    
class LevelAdmin(admin.ModelAdmin):
    form = LevelForm
    list_display = ['id','title','points_range_from','points_range_to']
    search_fields = ['title']

class MemberAdmin(ForeignKeyAutocompleteAdmin,DjangoMpttAdmin):
    form = MemberForm
    list_display = ['id',"user","parent","name","points","phone","gender","level","get_acoes"]
    list_display_links = ['id']
    search_fields = ['name']
    actions = ['delete_model']
    related_search_fields = {
       'user': ('first_name', 'email'),
       'parent': ('name'),
    }

    def get_actions(self, request):
        actions = super(MemberAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def delete_model(modeladmin, request, queryset):
        for obj in queryset:
            delete_user(obj)
            obj.user.delete()
            obj.delete()

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

    def get_acoes(self,obj):
        return '<a href="/upline/member/'+str(obj.id)+'/linear/">linear</a> <a href="/upline/member/'+str(obj.id)+'/binary/">binário</a> <a href="/upline/member/'+str(obj.id)+'/">editar</a>'

    get_acoes.short_description = 'Ações'
    get_acoes.allow_tags = True

class Invited(Member):
    class Meta:
        proxy = True

class InvitedAdmin(admin.ModelAdmin):
    form = MemberForm
    list_display = ['id',"user","parent","name","points","phone","gender"]
    list_display_links = ['id']
    search_fields = ['name']
    actions = ['delete_model']
    related_search_fields = {
       'user': ('first_name', 'email'),
       'parent': ('name'),
    }

    def get_actions(self, request):
        actions = super(InvitedAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

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
    list_display = ['id',"owner","name","state","city","phone","member"]
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
    list_display = ['id','name','active','points','table_value']

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
    # formset = # Yours

class SaleAdmin(ForeignKeyAutocompleteAdmin):
    list_display = ['id','member', 'client','create_time','total']
    
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

    def has_delete_permission(self, request, x = None):
        return False

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return list(set(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]
        ))

class CityAdmin(admin.ModelAdmin):
    list_display = ['id','state', 'name']
    search_fields = ['name']
    list_filter = ['state']

class StateAdmin(admin.ModelAdmin):
    list_display = ['id','acronym', 'name']
    search_fields = ['acronym', 'name']

class PostalCodeAdmin(ForeignKeyAutocompleteAdmin):
    related_search_fields = {
       'city': ('name'),
    }
    list_display = ['id','get_state','city','postal_code']
    search_fields = ['postal_code','city']
    list_filter = ['city__state']
    
    def get_state(self, obj):
        return obj.city.state

    get_state.short_description = 'State'
    get_state.admin_order_field = 'city__state'

# class EventAlertInline(admin.TabularInline):
#     model = EventAlert


# Create the filter
class EventDateFilter(SimpleListFilter):
    title = _('Data')
    parameter_name = 'begin_time'
    # Set the displaying options
    def lookups(self, request, model_admin):
        return (
            ('PREVIOUS', _('Previous')),
            ('AFTER', _('After')),
        )
    # Assign a query for each option
    def queryset(self, request, queryset):
        if self.value() == 'PREVIOUS':
            return queryset.filter(begin_time__lte=datetime.datetime.now())
        elif self.value() == 'AFTER':
            return queryset.filter(begin_time__gte=datetime.datetime.now())

class EventAdmin(ForeignKeyAutocompleteAdmin):
    form = EventForm
    list_display = ["id","title","calendar","begin_time","group"]
    search_fields = ['name']
    list_filter = [EventDateFilter]
    related_search_fields = {
       'owner': ('name'),
       'calendar': ('name'),
       'invited': ('name'),
       'members': ('name'),
    }

    def get_queryset(self, request):
        qs = super(EventAdmin, self).get_queryset(request)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs.filter(begin_time__gte=datetime.datetime.now())

    def get_related_filter(self, model, request):
        if not issubclass(model, Member):
            return super(EventAdmin, self).get_related_filter(
                model, request
            )
        return Q(member_type=0)

    # inlines = [
    #     EventAlertInline,
    # ]


class PostAdmin(ForeignKeyAutocompleteAdmin):
    list_display = ['user','title','group','content','create_time','media_type','get_media_file']
    form = PostForm
    related_search_fields = {
       'user': ('first_name', 'email'),
    }

    def get_media_file(self, obj):
        if obj.media_type == 0:
            return '<img src="'+obj.media+'" style="height:150px"/>'
        elif obj.media_type == 1:
            return '<audio src="'+obj.media+'" controls>Your browser does not support the <code>audio</code> element.</audio>'
        elif obj.media_type == 2:
            return '<video src="'+obj.media+'"/>'

    get_media_file.short_description = 'Arquivo'
    get_media_file.allow_tags = True

class CalendarAdmin(ForeignKeyAutocompleteAdmin):
    related_search_fields = {
       'user': ('first_name', 'email'),
    }

class MediaAdmin(admin.ModelAdmin):
    list_display = ['id','get_media_type','media_category','name','get_media_file']
    search_fields = ['name']
    list_filter = ['media_type']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('converted',)
        return self.readonly_fields

    def get_media_type(self, obj):
        return obj.get_media_type_display()

    def get_media_file(self, obj):
        if obj.media_type == 0:
            return '<img src="'+obj.media+'" style="height:150px"/>'
        elif obj.media_type == 1:
            return '<audio src="'+obj.media+'" controls>Your browser does not support the <code>audio</code> element.</audio>'
        elif obj.media_type == 2:
            return '<video src="'+obj.media+'"/>'

    get_media_file.short_description = 'Arquivo'
    get_media_file.allow_tags = True
    get_media_type.short_description = 'Media Type'
    get_media_type.admin_order_field = 'media_category__media_type'

class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']

class TrainingStepAdmin(admin.ModelAdmin):
    list_display = ["step","training","title","description"]
    search_fields = ['name']
    list_filter = ['training']
    form = TrainingStepForm

class AudioAdmin(admin.ModelAdmin):
    pass

class VideoAdmin(admin.ModelAdmin):
    pass
    
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id','level','message','sent','get_date_sent']
    actions = ['send']

    def get_date_sent(self,obj):
        if obj.sent:
            return obj.update_time
        else:
            return None

    get_date_sent.short_description = 'Data do Envio'

    def send(modeladmin, request, queryset):
        for notification in queryset:
            devices = GCMDevice.objects.filter(user__in=notification.level.user_set.all())
            devices.send_message(notification.message)
        queryset.update(sent=True)

    send.short_description = u"Enviar notificações"

# admin.site.register(Audio,AudioAdmin)
# admin.site.register(Video,VideoAdmin)
admin.site.register(Invited,InvitedAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(TrainingStep,TrainingStepAdmin)
admin.site.register(Training,TrainingAdmin)
admin.site.register(Level,LevelAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Goal,GoalAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Sale,SaleAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(State,StateAdmin)
admin.site.register(PostalCode,PostalCodeAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Calendar,CalendarAdmin)
admin.site.register(Media,MediaAdmin)
admin.site.register(MediaCategory,MediaCategoryAdmin)