# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmatapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieCate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mid', models.IntegerField()),
                ('dim', models.TextField(null=True, blank=True)),
                ('pids', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'movie_cate',
                'managed': False,
            },
        ),
    ]
