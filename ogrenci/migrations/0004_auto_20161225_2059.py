# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-25 20:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ogrenci', '0003_auto_20161210_1607'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ogrenci',
            options={'ordering': ['sinif', 'no']},
        ),
    ]
