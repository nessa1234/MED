# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-12 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doc_name', models.CharField(max_length=50)),
                ('Doc_age', models.IntegerField(default=18)),
                ('Doc_email', models.EmailField(max_length=254)),
                ('Doc_photo', models.ImageField(upload_to='media/staff_img')),
                ('Doc_Speciality', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
