# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from django.db import models

# Create your models here.


class DocumentTypes(models.Model):
    """Document types."""

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documentos"


class Documents(models.Model):
    """
        Documents.
    """

    title = models.CharField(max_length=200)
    document = models.FileField(upload_to='files/documents')
    type = models.ForeignKey('DocumentTypes')

    def __str__(self):
        return '%s-%s' % (self.title, self.type)

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"


class Person(models.Model):
    """
        Class base to inherit its fields to another model related with a Person.
    """

    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=37, unique=True, default='',
                                  help_text='Número de Identidad', verbose_name="Número de Identidad")
    picture = models.ImageField(
        upload_to='files/pictures', verbose_name="Archivo de Imágen")
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='',
                                help_text='Usuario para accesar desde el app', verbose_name="Usuario")
    phone = models.CharField(max_length=30, default='',
                             help_text='Número de teléfono', verbose_name="Teléfono")

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.picture))

    image_tag.short_description = 'Imágen'

    @property
    def full_name(self):
        """Returns person full name."""
        return '%s %s' % (self.user.first_name, self.user.last_name)

    class Meta:
        unique_together = ('identifier', 'phone')
