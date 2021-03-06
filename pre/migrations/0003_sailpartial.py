# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-26 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pre', '0002_auto_20181025_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='SailPartial',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('imo', models.CharField(blank=True, db_column='Imo', max_length=64, null=True)),
                ('flag', models.CharField(blank=True, db_column='Flag', max_length=128, null=True)),
                ('routeid', models.IntegerField(blank=True, db_column='RouteId', null=True)),
                ('departuretime', models.DateTimeField(blank=True, db_column='DepartureTime', null=True)),
                ('cargo', models.CharField(blank=True, db_column='Cargo', max_length=255, null=True)),
                ('capacity', models.CharField(blank=True, db_column='Capacity', max_length=128, null=True)),
                ('arrivetime', models.DateTimeField(blank=True, db_column='ArriveTime', null=True)),
                ('value', models.IntegerField(db_column='Value')),
            ],
            options={
                'db_table': 'sail_partial',
                'managed': True,
            },
        ),
    ]
