# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('url', models.URLField(verbose_name='url', max_length=255)),
                ('title', models.CharField(verbose_name='description', max_length=20)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('is_public', models.BooleanField(verbose_name='public', default=True)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('date_updated', models.DateTimeField(verbose_name='date updated')),
                ('owner', models.ForeignKey(verbose_name='owner', related_name='bookmarks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'bookmark',
                'verbose_name_plural': 'bookmarks',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tags',
            field=models.ManyToManyField(blank=True, to='marcadorapp.Tag'),
        ),
    ]
