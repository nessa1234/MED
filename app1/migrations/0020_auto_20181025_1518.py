# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-25 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_schedule_dc_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.DateField(default=None),
        ),
    ]
