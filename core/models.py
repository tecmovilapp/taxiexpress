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

    def __str__(self):
        return '%s-%s' % (self.title, self.type)


class Person(models.Model):
    """
        Class base to inherit its fields to another model related with a Person.
    """

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=120)
    picture = models.ImageField(upload_to='files/pictures')

    @property
    def full_name(self):
        """Returns person full name."""
        return '%s %s' % (self.first_name, self.last_name)
