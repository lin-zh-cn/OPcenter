# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-13 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saltstack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playbook',
            name='sls',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]