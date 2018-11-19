# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


# Create your models here.

class DocumentTypes(models.Model):
    """Document types."""

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return '%s' % self.title

class Documents(models.Model):
    """
        Documents.
    """

    title = models.CharField(max_length=200)
    document = models.FileField(upload_to='files/documents')
    type = models.ForeignKey('DocumentTypes')

    def __str__(self):
        return '%s-%s' % (self.title, self.type)

class Person(models.Model):
    """
        Class base to inherit its fields to another model related with a Person.
    """

    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=30, unique=True, default='')
    picture = models.ImageField(upload_to='files/pictures')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')

    @property
    def full_name(self):
        """Returns person full name."""
        return '%s %s' % (self.user.first_name, self.user.last_name)
