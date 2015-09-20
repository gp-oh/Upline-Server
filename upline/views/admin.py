# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
import inspect, json, datetime
from upline.models import *
from django.db.models import Count, Avg, Sum

class HomeView(View):
    def get(self,request):
        return render(request,'admin/index.html',{'sales':self.get_sales(),
            'member_levels':self.get_member_levels(),
            'contacts':self.get_contacts(),
            'members':self.get_members(),
            'clients':self.get_clients()})

    def get_contacts(self):
        from_date = datetime.datetime.today()-datetime.timedelta(days=30)
        to_date = datetime.datetime.today()
        contacts_per_day = Contact.objects.filter(contact_category=0,create_time__gte=from_date,create_time__lte=to_date).extra({'published':"date(create_time)"}).values('published').annotate(total=Count('id')).order_by('published')
        contacts_list = []
        i = -1
        for contact in contacts_per_day:
            if len(contacts_list) > 0 and contact['published']-datetime.timedelta(days=1) > contacts_list[-1]['published'] :
                while contacts_list[-1]['published'] < contact['published']-datetime.timedelta(days=1):
                    contacts_list.append({'published':contacts_list[-1]['published']+datetime.timedelta(days=1),'total':0.00})
            contacts_list.append({'published':contact['published'],'total':str(contact['total']).replace(',','.')})
        return contacts_list

    def get_members(self):
        from_date = datetime.datetime.today()-datetime.timedelta(days=30)
        to_date = datetime.datetime.today()
        members_per_day = Member.objects.filter(create_time__gte=from_date,create_time__lte=to_date).extra({'published':"date(create_time)"}).values('published').annotate(total=Count('id')).order_by('published')
        members_list = []
        i = -1
        for member in members_per_day:
            if len(members_list) > 0 and member['published']-datetime.timedelta(days=1) > members_list[-1]['published'] :
                while members_list[-1]['published'] < member['published']-datetime.timedelta(days=1):
                    members_list.append({'published':members_list[-1]['published']+datetime.timedelta(days=1),'total':0})
            members_list.append({'published':member['published'],'total':str(member['total']).replace(',','.')})
        return members_list

    def get_clients(self):
        from_date = datetime.datetime.today()-datetime.timedelta(days=30)
        to_date = datetime.datetime.today()
        contacts_per_day = Contact.objects.filter(contact_category=1,create_time__gte=from_date,create_time__lte=to_date).extra({'published':"date(create_time)"}).values('published').annotate(total=Count('id')).order_by('published')
        contacts_list = []
        i = -1
        for contact in contacts_per_day:
            if len(contacts_list) > 0 and contact['published']-datetime.timedelta(days=1) > contacts_list[-1]['published'] :
                while contacts_list[-1]['published'] < contact['published']-datetime.timedelta(days=1):
                    contacts_list.append({'published':contacts_list[-1]['published']+datetime.timedelta(days=1),'total':0})
            contacts_list.append({'published':contact['published'],'total':str(contact['total']).replace(',','.')})
        return contacts_list

    def get_sales(self):
        from_date = datetime.datetime.today()-datetime.timedelta(days=30)
        to_date = datetime.datetime.today()

        sales_per_day = Sale.objects.filter(create_time__gte=from_date,create_time__lte=to_date).extra({'published':"date(create_time)"}).values('published').annotate(total=Sum('total')).order_by('published')
        sales_list = []
        i = -1
        for sale in sales_per_day:
            if len(sales_list) > 0 and sale['published']-datetime.timedelta(days=1) > sales_list[-1]['published'] :
                while sales_list[-1]['published'] < sale['published']-datetime.timedelta(days=1):
                    sales_list.append({'published':sales_list[-1]['published']+datetime.timedelta(days=1),'total':str('0.00')})
            sales_list.append({'published':sale['published'],'total':str(sale['total']).replace(',','.')})
        return sales_list

    def get_member_levels(self):
        print Member.objects.all().values('level','level__color').annotate(total=Count('id')).order_by('total')
        return Member.objects.all().values('level','level__color').annotate(total=Count('id')).order_by('total')


