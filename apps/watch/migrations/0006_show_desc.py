# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-15 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0005_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='desc',
            field=models.TextField(default='No description created :('),
        ),
    ]
