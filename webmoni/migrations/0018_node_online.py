# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-22 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmoni', '0017_node_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='online',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
