# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-03 23:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='avatar',
        ),
    ]
