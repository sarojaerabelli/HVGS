# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 06:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CareerTinder', '0004_auto_20160918_0152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hiree',
            old_name='first_name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='hiree',
            old_name='last_name',
            new_name='name',
        ),
    ]
