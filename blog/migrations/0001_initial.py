# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome e Sobrenome do Editor')),
                ('facebooklink', models.CharField(verbose_name='Link do Facebook pessoal', null=True, max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(null=True, max_length=100, blank=True)),
                ('capa', models.ImageField(upload_to='img/', default='static/img/logo.svg', verbose_name='Foto da capa')),
                ('nivel', models.PositiveSmallIntegerField(null=True, default=1)),
                ('text1', models.TextField()),
                ('picture1', models.ImageField(upload_to='img/', blank=True)),
                ('picturefigcaption1', models.CharField(max_length=200, default='Direitos reservados', verbose_name='Figcaption')),
                ('text2', models.TextField(blank=True)),
                ('picture2', models.ImageField(upload_to='img/', blank=True)),
                ('picturefigcaption2', models.CharField(max_length=200, default='Direitos reservados', verbose_name='Figcaption')),
                ('text3', models.TextField(blank=True)),
                ('picture3', models.ImageField(upload_to='img/', blank=True)),
                ('picturefigcaption3', models.CharField(max_length=200, default='Direitos reservados', verbose_name='Figcaption')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('categoria', models.ForeignKey(null=True, to='blog.Categoria')),
                ('editor', models.ManyToManyField(to='blog.Editor')),
            ],
        ),
    ]
