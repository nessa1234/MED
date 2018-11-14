# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-24 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_auto_20181024_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='depart_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='Doc_Speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Department'),
        ),
    ]
