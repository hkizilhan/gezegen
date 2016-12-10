# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogrenci', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ogrenci',
            name='ad',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ogrenci',
            name='cinsiyet',
            field=models.CharField(choices=[('Erkek', 'Erkek'), ('Kız', 'Kız')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ogrenci',
            name='sinif',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ogrenci',
            name='soyad',
            field=models.CharField(max_length=50),
        ),
    ]