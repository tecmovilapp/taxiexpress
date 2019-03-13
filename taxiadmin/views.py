"""/taxiadmin/views.py"""
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from taxiadmin.forms import VehicleForm, MyForm
from taxiadmin.models import Vehicle

from google.cloud import firestore

import json

from django.http import HttpResponse, HttpResponseRedirect

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


@staff_member_required
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

@staff_member_required
def form_handle(request):
    if request.method == 'POST':
        form = MyForm(request.POST) # if post method then form will be validated
        if form.is_valid():
            cd = form.cleaned_data
            num1 = cd.get('num1')
            num2 = cd.get('num2')
            result = cd.get('result')
            if float(num1) + float(num2) == float(result):
                # give HttpResponse only or render page you need to load on success
                return HttpResponse("valid entiries")
            else:
                # if sum not equal... then redirect to custom url/page 
                return HttpResponseRedirect('/admin/taxiadmin/rides')  # mention redirect url in argument

    else:
        form = MyForm() # blank form object just to pass context if not post method

    
    context = admin.site.each_context(request)
    context.update({
        'title': 'Agrear Carrera',
        'form': form
    })
    return render(request, "rides/rides_add.html", context)