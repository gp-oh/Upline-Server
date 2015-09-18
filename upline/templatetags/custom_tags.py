# -*- coding: utf-8 -*-
from django import template
import inspect, json, datetime
register = template.Library()
from django.template.loader import render_to_string
from upline.models import *
from django.db.models import Count, Avg, Sum

def get_sales(list):
    from_date = datetime.datetime.today()-datetime.timedelta(days=30)
    to_date = datetime.datetime.today()

    sales_per_day = Sale.objects.filter(create_time__gte=from_date,create_time__lte=to_date).extra({'published':"date(create_time)"}).values('published').annotate(total=Sum('total')).order_by('published')
    sales_list = []
    i = -1
    for sale in sales_per_day:
        if len(sales_list) > 0 and sale['published']-datetime.timedelta(days=1) > sales_list[-1]['published'] :
            while sales_list[-1]['published'] < sale['published']-datetime.timedelta(days=1):
                sales_list.append({'published':sales_list[-1]['published']+datetime.timedelta(days=1),'total':0.00})
        sales_list.append({'published':sale['published'],'total':sale['total']})
    return sales_list

def get_member_levels():
    return Member.objects.all().values('level').annotate(total=Count('id')).order_by('total')