# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from core.preset_choices import DOCUMENT_TYPES

# Create your models here.

class Documents(models.Model):
    """
        Documents.
    """

    title = models.CharField(max_length=200)
    document = models.FileField(upload_to='files/documents')
    type = models.CharField(max_length=100, choices=DOCUMENT_TYPES)
