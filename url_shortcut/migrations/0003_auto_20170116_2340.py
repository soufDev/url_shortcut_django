# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 23:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortcut', '0002_auto_20170116_2334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miniurl',
            options={'verbose_name': 'Mini URL', 'verbose_name_plural': 'Minis URL'},
        ),
    ]