# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 18:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0010_order_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created',
        ),
    ]
