# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-26 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pre', '0003_sailpartial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sailpartial',
            name='value',
        ),
        migrations.AddField(
            model_name='routepartial',
            name='value',
            field=models.IntegerField(blank=True, db_column='Value', null=True),
        ),
    ]