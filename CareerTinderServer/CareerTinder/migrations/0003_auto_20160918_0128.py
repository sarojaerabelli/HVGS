# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 05:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CareerTinder', '0002_auto_20160918_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hiree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CareerTinder.Hiree')),
            ],
        ),
        migrations.RemoveField(
            model_name='recruiter',
            name='hirees',
        ),
        migrations.AddField(
            model_name='relations',
            name='recruiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CareerTinder.Recruiter'),
        ),
    ]
