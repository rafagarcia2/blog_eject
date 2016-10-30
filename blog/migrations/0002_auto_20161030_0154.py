# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 10, 30, 3, 53, 53, 169584, tzinfo=utc), verbose_name='Atalho'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 10, 30, 3, 54, 7, 656116, tzinfo=utc), verbose_name='Atalho'),
            preserve_default=False,
        ),
    ]
