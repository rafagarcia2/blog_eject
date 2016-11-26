# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnviarEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('assunto', models.CharField(max_length=200)),
                ('texto', models.TextField()),
            ],
        ),
    ]
