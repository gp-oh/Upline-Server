 # -*- coding: utf-8 -*-
from django.contrib import admin
from upline.models import *
from django_mptt_admin.admin import DjangoMpttAdmin

class TrainingAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']

class LevelAdmin(admin.ModelAdmin):
    list_display = ['id','title','points_range_from','points_range_to']
    search_fields = ['title']

class MemberAdmin(DjangoMpttAdmin):
    list_display = ['id',"user","parent","name","points","phone","gender","level","get_acoes"]
    list_display_links = None
    search_fields = ['name']

    def get_acoes(self,obj):
        return '<a href="/admin/upline/member/'+str(obj.id)+'/linear/">linear</a> <a href="/admin/upline/member/'+str(obj.id)+'/binary/">binário</a> <a href="/admin/upline/member/'+str(obj.id)+'/">editar</a>'

    get_acoes.short_description = 'Ações'
    get_acoes.allow_tags = True


class TeamAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

class GoalAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

class SaleAdmin(admin.ModelAdmin):
    pass

class CityAdmin(admin.ModelAdmin):
    list_display = ['id','state', 'name']
    search_fields = ['name']
    list_filter = ['state']

class StateAdmin(admin.ModelAdmin):
    list_display = ['id','acronym', 'name']
    search_fields = ['acronym', 'name']

class PostalCodeAdmin(admin.ModelAdmin):
    list_display = ['id','get_state','city','postal_code']
    search_fields = ['postal_code','city']
    list_filter = ['city__state']
    
    def get_state(self, obj):
        return obj.city.state

    get_state.short_description = 'State'
    get_state.admin_order_field = 'city__state'

class EventAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CalendarAdmin(admin.ModelAdmin):
    pass

class MediaAdmin(admin.ModelAdmin):
    list_display = ['id','get_media_type','media_category','name']
    search_fields = ['name']
    list_filter = ['media_category__media_type']

    def get_media_type(self, obj):
        return obj.media_category.get_media_type_display()

    get_media_type.short_description = 'Media Type'
    get_media_type.admin_order_field = 'media_category__media_type'

class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','media_type','name']
    search_fields = ['name']
    list_filter = ['media_type']

admin.site.register(TrainingStep)
admin.site.register(Training,TrainingAdmin)
admin.site.register(Level,LevelAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Team,TeamAdmin)
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