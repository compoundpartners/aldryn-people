# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 17:20
from __future__ import unicode_literals

import aldryn_common.admin_fields.sortedm2m
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_people', '0032_person_companies'),
        ('js_locations', '0001_initial'),
    ]

    database_operations = [
        migrations.AlterModelTable('Location', 'js_locations_location'),
        migrations.AlterModelTable('LocationTranslation', 'js_locations_location_translation')
    ]

    state_operations = [
        #migrations.AlterUniqueTogether(
            #name='locationtranslation',
            #unique_together=set([]),
        #),
        #migrations.RemoveField(
            #model_name='locationtranslation',
            #name='master',
        #),
        migrations.AlterField(
            model_name='person',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='js_locations.Location', verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='relatedpeopleplugin',
            name='related_locations',
            field=aldryn_common.admin_fields.sortedm2m.SortedM2MModelField(blank=True, help_text=None, to='js_locations.Location', verbose_name='related locations'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='LocationTranslation',
        ),
    ]


    operations = [
      migrations.SeparateDatabaseAndState(
        database_operations=database_operations,
        state_operations=state_operations)
    ]
