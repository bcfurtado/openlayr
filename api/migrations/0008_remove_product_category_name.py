# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-17 23:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_migrate_category_name_column_to_category_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_name',
        ),
    ]
