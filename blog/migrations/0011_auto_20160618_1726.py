# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-18 20:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160618_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Editor',
            new_name='editor',
        ),
    ]
