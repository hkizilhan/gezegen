# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ustyazi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosya_no', models.CharField(max_length=20)),
                ('sayi_no', models.CharField(max_length=20)),
                ('tarih', models.DateField()),
                ('konu', models.CharField(max_length=200)),
                ('nereye', models.CharField(max_length=200)),
                ('ilgi', models.CharField(blank=True, max_length=200)),
                ('yazi', models.CharField(max_length=200)),
                ('ek', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
