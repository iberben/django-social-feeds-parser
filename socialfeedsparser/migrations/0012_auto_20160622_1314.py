# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-22 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialfeedsparser', '0011_auto_20160131_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Is Active'),
        ),
    ]