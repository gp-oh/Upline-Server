# -*- coding: utf-8 -*-
from django import template
import inspect, json, datetime
register = template.Library()
from django.template.loader import render_to_string
from upline.models import *
from django.db.models import Count, Avg, Sum

@register.filter
def get_sales(f = False,t = False):
    if f:
        from_date = datetime.datetime.strptime(f, '%d/%m/%Y')
    else:
        from_date = datetime.datetime.today()-datetime.timedelta(days=30)

    if t:
        to_date = datetime.datetime.strptime(t, '%d/%m/%Y')
    else:
        to_date = datetime.datetime.today()

    sales = Sale.objects.filter(create_time__gte=from_date,create_time__lte=to_date)
    totals = {}
    for sale in sales:
        if not sale.created.strftime("%Y-%M-%d") in totals:
            totals[sale.created.strftime("%Y-%M-%d")] = sale.total
        else:
            totals[sale.created.strftime("%Y-%M-%d")] += sale.total
    return totals

def get_member_levels():
    return Member.objects.all().values('level').annotate(total=Count('id')).order_by('total')