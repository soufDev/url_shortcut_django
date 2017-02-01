# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortcut', '0003_auto_20170116_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniurl',
            name='default_url',
            field=models.URLField(max_length=150, unique=True, verbose_name=b'Enter the URL'),
        ),
        migrations.AlterField(
            model_name='miniurl',
            name='identifier_create',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Identifier'),
        ),
    ]