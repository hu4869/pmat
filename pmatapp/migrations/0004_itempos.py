# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmatapp', '0003_itemtopiccut'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itempos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.FloatField(null=True, blank=True)),
                ('y', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'itempos',
                'managed': False,
            },
        ),
    ]
