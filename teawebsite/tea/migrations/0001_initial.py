# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('name', models.CharField(help_text='Enter the name of the tea.', max_length=200, primary_key=True, serialize=False)),
            ],
        ),
    ]
