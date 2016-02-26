# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Itemneigh',
            fields=[
                ('mid', models.IntegerField(serialize=False, primary_key=True)),
                ('list', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'itemneigh',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Itemtopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'itemtopic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('rate_ave', models.FloatField(null=True, blank=True)),
                ('genres', models.TextField(null=True, blank=True)),
                ('keyword', models.TextField(null=True, blank=True)),
                ('revenue', models.IntegerField(null=True, blank=True)),
                ('overview', models.TextField(null=True, blank=True)),
                ('rate_cnt', models.IntegerField(null=True, blank=True)),
                ('popularity', models.FloatField(null=True, blank=True)),
                ('mid', models.IntegerField(serialize=False, primary_key=True)),
                ('poster', models.CharField(max_length=100, null=True, blank=True)),
                ('crew', models.TextField(null=True, blank=True)),
                ('releasedate', models.DateField(null=True, blank=True)),
                ('cast', models.TextField(null=True, blank=True)),
                ('studio', models.TextField(null=True, blank=True)),
                ('budget', models.IntegerField(null=True, blank=True)),
                ('title', models.CharField(max_length=80, null=True, blank=True)),
                ('runtime', models.IntegerField(null=True, blank=True)),
                ('homepage', models.CharField(max_length=80, null=True, blank=True)),
                ('trailer', models.CharField(max_length=80, null=True, blank=True)),
            ],
            options={
                'db_table': 'movie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Plink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'plink',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pid', models.AutoField(serialize=False, primary_key=True)),
                ('val', models.TextField(null=True, blank=True)),
                ('dim', models.TextField(null=True, blank=True)),
                ('count', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'profile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('tid', models.IntegerField(serialize=False, primary_key=True)),
                ('eff_num_words', models.FloatField(null=True, blank=True)),
                ('rank_1_docs', models.FloatField(null=True, blank=True)),
                ('coherence', models.FloatField(null=True, blank=True)),
                ('uniform_dist', models.FloatField(null=True, blank=True)),
                ('tokens', models.FloatField(null=True, blank=True)),
                ('document_entropy', models.FloatField(null=True, blank=True)),
                ('corpus_dist', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'topic',
                'managed': False,
            },
        ),
    ]
