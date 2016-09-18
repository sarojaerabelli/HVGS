# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 07:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CareerTinder', '0013_auto_20160918_0328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hiree',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='hiree',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='relations',
            name='encounter_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 18, 3, 38, 0, 29620)),
        ),
    ]