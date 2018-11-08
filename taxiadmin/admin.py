# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.admin import AdminSite
from django.http import HttpResponse
from django.conf.urls import url
from django.contrib import admin

from django.utils.html import format_html
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from . import views
# Register your models here.

from taxiadmin.models import Driver, VehicleMaker, VehicleModel, Vehicle, VehicleAssignment


admin.site.register(Driver)
admin.site.register(VehicleMaker)

def edit_vehicle(modeladmin, request, queryset):
    pass

edit_vehicle.short_description = 'edit car'    

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('register', 'year', 'made', 'model', 'edit_action')
    list_filter = ('number', 'year')
    search_fields = ['number', 'register']

    def get_urls(self):
        urls = super(VehicleAdmin, self).get_urls()
        custom_urls = [
            url(
                r'^(?P<vehicle_id>.+)/edit/$',
                self.admin_site.admin_view(views.locate_view),
                name='vehicle-edit',
            ),
        ]
        return custom_urls + urls
    

    def edit_action(self, obj):
        return format_html(
            '<a class="btn btn-primary" href="{}">locate</a>',
            reverse('admin:vehicle-edit', args=[obj.pk]),
        )

    edit_action.allow_tags = True
    edit_action.short_description = "Actions"


@admin.register(VehicleAssignment)
class VehicleAssignmentAdmin(admin.ModelAdmin):
    search_fields = ['vehicle__register']
    list_display = ('vehicle', 'driver')


@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    search_fields = ('made__title',)

