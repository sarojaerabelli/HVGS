# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CareerTinder', '0005_auto_20160918_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiree',
            name='degree',
            field=models.CharField(choices=[(b'BA', b'B.A./B.S.'), (b'MA', b'M.A./M.S.'), (b'DO', b'Ph.D. or Higher')], max_length=10),
        ),
    ]
