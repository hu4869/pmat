# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmatapp', '0004_itempos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topicdist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tid1', models.IntegerField(null=True, blank=True)),
                ('tid2', models.IntegerField(null=True, blank=True)),
                ('dist', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'topicdist',
                'managed': False,
            },
        ),
    ]
