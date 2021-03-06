# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tea', '0002_tea_gal_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrewingMethod',
            fields=[
                ('name', models.CharField(help_text='Enter the name of this brewing method.', max_length=200, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=2000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='tea',
            name='description',
            field=models.TextField(help_text='Tea details', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='tea',
            name='m_image',
            field=models.ImageField(default='', upload_to='imgs'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='gal_img',
            field=models.ImageField(default='', upload_to='imgs'),
        ),
    ]
