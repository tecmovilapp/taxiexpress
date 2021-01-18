# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.admin import AdminSite
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect
from django.conf.urls import url
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
from django import forms
from django.forms import ModelForm, Form
from . import views

# Register your models here.
from taxiadmin.models import Driver, VehicleMaker, VehicleModel, Vehicle, Passenger, Purchase
from taxiadmin.forms import DriverForm

from django.utils.translation import ugettext as _

admin.site.site_header = 'Seven'

class AdminFancyPreview(object):
    '''
    This will add a thumbnail image, a fancy preview for your Django admin
    list page. Let's say you have a model that has an image field. With this
    helper you will be able to display a thumbnail in the admin list page.
    For example:
        class ProductAdmin(AdminFancyPreview, admin.ModelAdmin):
            list_display = ('name', 'preview')
    By default we will assume that you have an image field named `image`.
    If that's not the case, you will have to customize things.
        class ProductAdmin(AdminFancyPreview, admin.ModelAdmin):
            list_display = ('name', 'preview')
            fancy_preview = {
                'image_field': 'photo',
                'image_size': '60px',
            }
    Note how you can customize the image field name but also the thumbnail size
    by defining a `fancy_preview` dictionary.
    '''

    def preview(self, obj):
        template = u"""<img src="{url}" style="max-height: {size}; max-width: {size};" />"""
        config = {
            'image_field': 'picture',
            'image_size': '50px',
        }
        custom_config = getattr(self, 'fancy_preview', {})
        config.update(custom_config)
        picture = getattr(obj, config['image_field'], None)
        url = picture.url if picture else '/static/taxiadmin/driver/css/driver_admin_changelist.css'
        return template.format(url=url, size=config['image_size'])
    preview.short_description=_('Imagen')
    preview.allow_tags = True

class DriverAdmin(AdminFancyPreview, admin.ModelAdmin):
    list_display = ('preview', 'user', 'vehicle')
    fields = ['user', 'vehicle', 'image_tag', 'picture', 'identifier', 'phone', 'rating', 'related_documents']
    readonly_fields = ['image_tag', 'rating']           
    filter_horizontal = ('related_documents',)
    def get_form(self, request, obj=None, **kwargs): 
        self.form = DriverForm
        return super(DriverAdmin, self).get_form(request, obj, **kwargs) 

    def user(self,obj):
        return obj.get_value()

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
                r'^(?P<vehicle_id>.+)/locate/$',
                self.admin_site.admin_view(views.locate_view),
                name='vehicle-locate',
            ),
        ]
        return custom_urls + urls
    

    def edit_action(self, obj):
        return format_html(
            '<a class="btn btn-primary btn-sm" href="{}">Ubicar</a>',
            reverse('admin:vehicle-locate', args=[obj.pk]),
        )

    edit_action.allow_tags = True
    edit_action.short_description = "Actions"


#@admin.register(VehicleAssignment)
#class VehicleAssignmentAdmin(admin.ModelAdmin):
#    search_fields = ['vehicle__register']
#    list_display = ('vehicle', 'driver')


@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    search_fields = ('made__title',)
  

admin.site.register(Driver, DriverAdmin)
admin.site.register(VehicleMaker)
admin.site.register(Passenger)
admin.site.register(Purchase)
# admin.site.unregister(User)
# admin.site.unregister(Group)