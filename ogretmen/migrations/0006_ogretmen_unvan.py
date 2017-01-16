# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-15 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogretmen', '0005_auto_20170101_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='ogretmen',
            name='unvan',
            field=models.CharField(choices=[('MÜDÜR', 'Okul Müdürü'), ('MÜDÜR BAŞ YARDIMCISI', 'Müdür Baş Yardımcısı'), ('MÜDÜR YARDIMCISI', 'Müdür Yardımcısı'), ('ALAN ŞEFİ', 'Alan Şefi'), ('ÖĞRETMEN', 'Öğretmen')], default='ÖĞRETMEN', max_length=50),
        ),
    ]
