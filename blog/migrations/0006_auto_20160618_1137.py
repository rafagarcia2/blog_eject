# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-18 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160618_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author1',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ManyToManyField(to='blog.Editor'),
        ),
    ]
