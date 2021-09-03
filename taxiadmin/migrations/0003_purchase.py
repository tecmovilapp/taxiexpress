# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2021-01-11 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxiadmin', '0002_auto_20191010_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MerID', models.IntegerField(max_length=15)),
                ('AcqID', models.IntegerField(max_length=11)),
                ('OrderID', models.CharField(max_length=150)),
                ('ResponseCode', models.IntegerField(max_length=1)),
                ('ReasonCode', models.IntegerField(max_length=4)),
                ('ReasonCodeDesc', models.CharField(max_length=100)),
                ('ReferenceNo', models.IntegerField(max_length=12)),
                ('PaddedCardNo', models.IntegerField(max_length=19)),
                ('AuthCode', models.CharField(max_length=6)),
                ('CVV2Result', models.CharField(max_length=1)),
                ('ShipToFirstName', models.CharField(max_length=30)),
                ('ShipToLastName', models.CharField(max_length=30)),
                ('ShipToCountry', models.IntegerField(max_length=3)),
                ('ShipToEmail', models.CharField(max_length=50)),
                ('OriginalResponseCode', models.CharField(max_length=3)),
                ('Signature', models.CharField(max_length=28)),
                ('SignatureMethod', models.CharField(max_length=4)),
            ],
        ),
    ]
