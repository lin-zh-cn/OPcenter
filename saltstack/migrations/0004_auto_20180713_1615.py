# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-13 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saltstack', '0003_auto_20180713_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='async_jobs',
            name='status',
            field=models.IntegerField(choices=[(0, '排队中'), (1, '执行中'), (2, '已完成')], default=0),
        ),
    ]
