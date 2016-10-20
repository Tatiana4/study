# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 13:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='data',
            new_name='article_data',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='likes',
            new_name='article_likes',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='text',
            new_name='article_text',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='article_title',
        ),
    ]