# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from core.models import Documents, Person
from core.preset_choices import VEHICLE_STATUS

class VehicleMaker(models.Model):
    """
        Vehicle Makers eg: Toyota, Mitsubishi, etc.
    """

    title = models.CharField(max_length=100, help_text='Titulo de la marca (Ej: Toyota)')

    def __str__(self):
        """Return the title"""
        return self.title
        
    class Meta:
        verbose_name = "Marca de Vehículo"
        verbose_name_plural = "Marcas de Vehículos"


class VehicleModel(models.Model):
    """
        Model: eg, Corolla, Lancer, etc.
    """

    title = models.CharField(max_length=100, help_text='Titulo del modelo (Ej: Corolla)')
    made = models.ForeignKey('VehicleMaker', on_delete=models.CASCADE, help_text='Marca del Vehiculo')

    def __str__(self):
        """Return the title"""
        return self.title

    class Meta:
        verbose_name = "Modelo de Vehículo"
        verbose_name_plural = "Modelos de Vehículos"


class Vehicle(models.Model):
    """
        Describe a taxi.
    """

    register = models.CharField(max_length=30, help_text='Placa del Vehiculo')
    number = models.CharField(max_length=10, help_text='Numero de taxi')
    year = models.CharField(max_length=8, blank=True, null=True, help_text='Año del Vehiculo')
    vin = models.CharField(max_length=30, blank=True, null=True, help_text='Numero de Vin (Puede ser encontrado en la boleta de revision)')
    color = models.CharField(max_length=100, blank=True, null=True, help_text='Color')
    made = models.ForeignKey('VehicleMaker', on_delete=models.CASCADE, help_text='Marca del Vehiculo')
    model = models.ForeignKey('VehicleModel', on_delete=models.CASCADE, help_text='Modelo del Vehiculo')

    def __str__(self):
        """Return the title"""
        return '{0}-{1}'.format(self.model, self.number)

    class Meta:
        unique_together = ('register',)
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"


class Driver(Person):
    """
        Define a person who can drive a taxi.
    """
    rating = models.FloatField(default=0, help_text='Rating del conductor', verbose_name = "Rating")
    related_documents = models.ManyToManyField(
        Documents, 
        help_text='Documentos asociados al conductor',
        verbose_name="Documentos")
    vehicle = models.OneToOneField(Vehicle, default=None, null=True, blank=True, help_text='El vehículo asignado al conductor', verbose_name="Vehículo")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Conductor"
        verbose_name_plural = "Conductores"
    

class Passenger(Person):
    """
        Costumer model
    """

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Pasajero"
        verbose_name_plural = "Pasajeros"



