# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-15 18:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0002_auto_20190415_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='Network',
            new_name='network',
        ),
    ]
