# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from taxiadmin.models import Driver, VehicleMaker, VehicleModel, Vehicle


admin.site.register(Driver)
admin.site.register(VehicleMaker)
admin.site.register(VehicleModel)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_filter = ('number', 'year')
    search_fields = ['number', 'register']
