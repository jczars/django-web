# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
