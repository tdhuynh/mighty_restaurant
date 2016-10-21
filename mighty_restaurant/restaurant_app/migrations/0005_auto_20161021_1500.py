# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0004_auto_20161021_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='access_level',
            field=models.CharField(blank=True, choices=[('o', 'owner'), ('s', 'server'), ('c', 'cook')], max_length=1, null=True),
        ),
    ]
