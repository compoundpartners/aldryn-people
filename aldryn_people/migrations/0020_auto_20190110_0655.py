# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-10 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_people', '0019_auto_20180619_0559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persontranslation',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='persontranslation',
            name='first_name',
            field=models.CharField(default='', help_text="Provide this person's name.", max_length=255, verbose_name='name'),
        ),
    ]
