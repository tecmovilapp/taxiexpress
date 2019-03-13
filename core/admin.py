# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import Documents, DocumentTypes

# Register your models here.

admin.site.register(DocumentTypes)
admin.site.register(Documents)
