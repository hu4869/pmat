# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmatapp', '0005_topicdist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catetopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pid', models.IntegerField(null=True, blank=True)),
                ('tid', models.IntegerField(null=True, blank=True)),
                ('weight', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'catetopic',
                'managed': False,
            },
        ),
    ]
