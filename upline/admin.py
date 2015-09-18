 # -*- coding: utf-8 -*-
from django.contrib import admin
from upline.models import *
from upline.forms import *
from django_mptt_admin.admin import DjangoMpttAdmin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from django.conf import settings

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
    related_search_fields = {
       'user': ('first_name', 'email'),
       'parent': ('name'),
    }

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('quickblox_id',)
        return self.readonly_fields

    def get_acoes(self,obj):
        return '<a href="/upline/member/'+str(obj.id)+'/linear/">linear</a> <a href="/upline/member/'+str(obj.id)+'/binary/">binário</a> <a href="/upline/member/'+str(obj.id)+'/">editar</a>'

    get_acoes.short_description = 'Ações'
    get_acoes.allow_tags = True


class ContactAdmin(ForeignKeyAutocompleteAdmin):
    related_search_fields = {
       'owner': ('name'),
       'member': ('name'),
    }

class GoalAdmin(ForeignKeyAutocompleteAdmin):
    related_search_fields = {
       'member': ('name'),
    }

class ProductAdmin(admin.ModelAdmin):
    pass

class SaleAdmin(ForeignKeyAutocompleteAdmin):
    related_search_fields = {
       'member': ('name'),
       'client': ('name'),
    }

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

class EventAdmin(ForeignKeyAutocompleteAdmin):
    form = EventForm
    related_search_fields = {
       'owner': ('name'),
       'calendar': ('name'),
       'invited': ('name'),
       'members': ('name'),
    }

class PostAdmin(ForeignKeyAutocompleteAdmin):
    form = PostForm
    related_search_fields = {
       'user': ('first_name', 'email'),
    }

class CalendarAdmin(ForeignKeyAutocompleteAdmin):
    related_search_fields = {
       'user': ('first_name', 'email'),
    }

class MediaAdmin(admin.ModelAdmin):
    list_display = ['id','get_media_type','media_category','name','get_media_file']
    search_fields = ['name']
    list_filter = ['media_category__media_type']

    def get_media_type(self, obj):
        return obj.media_category.get_media_type_display()

    def get_media_file(self, obj):
        if obj.media_category.media_type == 0:
            return '<img src="'+obj.media+'"/>'
        elif obj.media_category.media_type == 1:
            return '<audio src="'+obj.media+'" controls>Your browser does not support the <code>audio</code> element.</audio>'
        elif obj.media_category.media_type == 2:
            return '<video src="'+obj.media+'"/>'

    get_media_file.short_description = 'Arquivo'
    get_media_file.allow_tags = True
    get_media_type.short_description = 'Media Type'
    get_media_type.admin_order_field = 'media_category__media_type'

class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','media_type','name']
    search_fields = ['name']
    list_filter = ['media_type']

class TrainingStepAdmin(admin.ModelAdmin):
    form = TrainingStepForm

class AudioAdmin(admin.ModelAdmin):
    pass

class VideoAdmin(admin.ModelAdmin):
    pass
    
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id','level','message','sent','date_sent']
    actions = ['send']

    def get_date_sent(self,request,obj):
        if self.sent:
            return self.update_time
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