# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-01 21:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ogretmen', '0004_auto_20170101_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ogretmen',
            old_name='isdihdam',
            new_name='istihdam',
        ),
    ]