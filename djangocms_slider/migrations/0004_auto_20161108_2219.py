# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-08 21:19
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_slider', '0003_auto_20160728_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=pyuploadcare.dj.models.ImageField(),
        ),
    ]
