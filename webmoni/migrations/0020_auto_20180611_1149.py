# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-11 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmoni', '0019_auto_20180523_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='domainname',
            name='interval',
            field=models.ImageField(default=300, upload_to=''),
        ),
        migrations.AddField(
            model_name='domainname',
            name='trigger',
            field=models.ImageField(default=2, upload_to=''),
        ),
    ]
