# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-25 02:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_loginreg_registable'),
    ]

    operations = [
        migrations.DeleteModel(
            name='loginreg',
        ),
    ]
