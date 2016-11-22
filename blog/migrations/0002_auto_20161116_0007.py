# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='capa',
            field=models.ImageField(help_text='Palavras chaves separadas por vírgula', upload_to='img/', default='static/img/logo.svg', verbose_name='Foto da capa'),
        ),
    ]
