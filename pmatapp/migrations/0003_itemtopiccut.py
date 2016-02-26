# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmatapp', '0002_moviecate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemtopicCut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'itemtopic_cut',
                'managed': False,
            },
        ),
    ]
