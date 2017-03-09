# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-07 00:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtm', '0005_availabilityshare_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabilityshare',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0, 60), null=True),
        ),
    ]
