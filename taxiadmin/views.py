"""/taxiadmin/views.py"""
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.
# @staff_member_required
def locate_view(request, vehicle_id):
    """
    If you're using multiple admin sites with independent views you'll need to set
    current_app manually and use correct admin.site
    # request.current_app = 'admin'
    """
    context = admin.site.each_context(request)
    context.update({
        'title': 'Vehicle Localization',
    })

    template = 'vehicles/locate.html'
    return render(request, template, context)
