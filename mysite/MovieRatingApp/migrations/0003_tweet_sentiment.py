# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-09 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieRatingApp', '0002_auto_20170302_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='sentiment',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
