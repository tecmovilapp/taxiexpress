"""/taxiadmin/views.py"""
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from taxiadmin.forms import VehicleForm
from taxiadmin.models import Vehicle

from google.cloud import firestore

import json

# Create your views here.
def locations_view(request):
    """
    If you're using multiple admin sites with independent views you'll need to set
    current_app manually and use correct admin.site
    # request.current_app = 'admin'
    """
    vehicles = Vehicle.objects.all()

    context = admin.site.each_context(request)
    context.update({
        'title': 'Ubicaciones',
        'vehicles': vehicles
    })
    template = 'vehicles/locations.html'
    return render(request, template, context)

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
    obj_vehicle = Vehicle.objects.get(pk=vehicle_id)

    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=obj_vehicle)
        if form.is_valid():
            form.save() 
    else:
        form = VehicleForm(instance=obj_vehicle)
    
    context.update({
        'title': 'Vehicle Localization',
        'vehicleForm': form,
        'vehicleId': vehicle_id
    })


    template = 'vehicles/locate.html'
    return render(request, template, context)


# @staff_member_required
def rides_admin_view(request):
    """
    If you're using multiple admin sites with independent views you'll need to set
    current_app manually and use correct admin.site
    # request.current_app = 'admin'
    """
    db = firestore.Client()
    rides_ref = db.collection(u'rides')
    rides = rides_ref.get()    

    context = admin.site.each_context(request)
    context.update({
        'title': 'Carreras Disponibles',
        'rides': rides
    })

    template = 'rides/rides_list.html'
    return render(request, template, context)
