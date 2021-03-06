# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-14 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ayar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50, unique=True)),
                ('bolum', models.CharField(choices=[('genel', 'Genel Ayarlar')], max_length=200)),
                ('tur', models.CharField(max_length=200)),
                ('deger', models.CharField(max_length=200)),
            ],
            options={
                'default_permissions': ('ekle', 'güncelle', 'sil', 'görüntüle'),
            },
        ),
    ]
