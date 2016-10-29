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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome e Sobrenome do Editor')),
                ('facebooklink', models.CharField(blank=True, null=True, max_length=200, verbose_name='Link do Facebook pessoal')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(blank=True, null=True, max_length=100)),
                ('capa', models.ImageField(upload_to='img/', default='static/img/logo.svg', verbose_name='Foto da capa')),
                ('nivel', models.PositiveSmallIntegerField(null=True, default=1)),
                ('text1', models.TextField()),
                ('picture1', models.ImageField(blank=True, upload_to='img/')),
                ('picturefigcaption1', models.CharField(default='Direitos reservados', max_length=200, verbose_name='Figcaption')),
                ('text2', models.TextField(blank=True)),
                ('picture2', models.ImageField(blank=True, upload_to='img/')),
                ('picturefigcaption2', models.CharField(default='Direitos reservados', max_length=200, verbose_name='Figcaption')),
                ('text3', models.TextField(blank=True)),
                ('picture3', models.ImageField(blank=True, upload_to='img/')),
                ('picturefigcaption3', models.CharField(default='Direitos reservados', max_length=200, verbose_name='Figcaption')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('categoria', models.ForeignKey(to='blog.Categoria', null=True)),
                ('editor', models.ManyToManyField(to='blog.Editor')),
            ],
        ),
    ]
