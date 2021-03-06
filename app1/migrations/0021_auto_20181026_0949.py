# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-26 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_auto_20181025_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='Doc_Speciality',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app1.Department'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.TimeField(blank=True),
        ),
    ]
