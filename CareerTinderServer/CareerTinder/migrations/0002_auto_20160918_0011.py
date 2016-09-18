# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 04:11
from __future__ import unicode_literals

import CareerTinder.listfield
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CareerTinder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hiree',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='hiree',
            name='name',
        ),
        migrations.AddField(
            model_name='hiree',
            name='college',
            field=models.CharField(default='mit', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hiree',
            name='degree',
            field=models.CharField(choices=[(b'BA', b"Bachelor's"), (b'MA', b"Master's"), (b'DO', b'Doctorate')], default='ba', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hiree',
            name='first_name',
            field=models.CharField(default='john', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hiree',
            name='last_name',
            field=models.CharField(default='doe', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hiree',
            name='major',
            field=models.CharField(default='cs', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hiree',
            name='year',
            field=models.IntegerField(default='2019'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recruiter',
            name='hirees',
            field=CareerTinder.listfield.ListField(default=b''),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to=b'media/logos/'),
        ),
        migrations.AlterField(
            model_name='hiree',
            name='face_picture',
            field=models.ImageField(upload_to=b'media/faces/'),
        ),
        migrations.AlterField(
            model_name='hiree',
            name='resume_picture',
            field=models.FileField(upload_to=b'media/resumes/'),
        ),
    ]