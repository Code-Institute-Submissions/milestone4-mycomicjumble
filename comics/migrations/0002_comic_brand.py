# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-09 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='brand',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
