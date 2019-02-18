# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from core.models import Documents, Person
from core.preset_choices import VEHICLE_STATUS

class VehicleMaker(models.Model):
    """
        Vehicle Makers eg: Toyota, Mitsubishi, etc.
    """

    title = models.CharField(max_length=100)

    def __str__(self):
        """Return the title"""
        return self.title


class VehicleModel(models.Model):
    """
        Model: eg, Corolla, Lancer, etc.
    """

    title = models.CharField(max_length=100)
    made = models.ForeignKey('VehicleMaker', on_delete=models.CASCADE)

    def __str__(self):
        """Return the title"""
        return self.title


class Vehicle(models.Model):
    """
        Describe a taxi.
    """

    register = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    year = models.CharField(max_length=8, blank=True, null=True)
    vin = models.CharField(max_length=30, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, choices=VEHICLE_STATUS)
    made = models.ForeignKey('VehicleMaker', on_delete=models.CASCADE)
    model = models.ForeignKey('VehicleModel', on_delete=models.CASCADE)

    def __str__(self):
        """Return the title"""
        return '{0}-{1}'.format(self.model, self.number)


class Driver(Person):
    """
        Define a person who can drive a taxi.
    """

    related_documents = models.ManyToManyField(Documents)
    vehicle = models.OneToOneField(Vehicle, default=None, null=True, blank=True)

    def __str__(self):
        return self.full_name

