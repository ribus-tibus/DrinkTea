# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tea', '0007_auto_20171006_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='tea',
            name='image_name2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
