# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161030_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='keywords',
            field=models.CharField(help_text='Palavras chaves separadas por vírgula', null=True, blank=True, max_length=150, verbose_name='Keywords'),
        ),
    ]
