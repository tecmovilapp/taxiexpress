# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-18 01:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxiadmin', '0003_auto_20190110_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicleassignment',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='vehicleassignment',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='driver',
            name='vehicle',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='taxiadmin.Vehicle'),
        ),
        migrations.DeleteModel(
            name='VehicleAssignment',
        ),
    ]
