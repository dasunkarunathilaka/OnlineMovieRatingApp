# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-02 18:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieRatingApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tweets',
            new_name='Tweet',
        ),
    ]
