# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-14 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0004_auto_20160512_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paguser',
            name='color',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='paguser',
            name='size',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='paguser',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
