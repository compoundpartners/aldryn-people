# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-23 18:36
from __future__ import unicode_literals

from django.db import migrations
from aldryn_people.models import Person as PersonModel

# from django.conf import settings
# from django.core.exceptions import ObjectDoesNotExist
# from django.db import models, migrations


def forwards_func(apps, schema_editor):
    """
    These translation objects probably already exist, so, we need to carefully
    copy new field values into them.
    """
    Person = apps.get_model('aldryn_people', 'Person')
    # PersonTranslation = apps.get_model('aldryn_people', 'PersonTranslation')

    for obj in Person.objects.all():
        # PersonTranslation.objects.update_or_create(
        #     master_id=obj.pk,
        #     language_code=settings.LANGUAGE_CODE,
        #     defaults={
        #         "name": obj.name,
        #         "slug": obj.slug,
        #     }
        # )

        # obj.first_name_new = obj.first_name
        # obj.last_name_new = obj.last_name
        # AttributeError: 'Person' object has no attribute 'first_name'

        # obj.first_name_new = obj.safe_translation_getter(
        #         'first_name',
        #         default='',
        #         any_language=True
        # )
        # obj.last_name_new = obj.safe_translation_getter(
        #         'last_name',
        #         default='',
        #         any_language=True
        # )

        # p = PersonModel.objects.filter(id=obj.id).first()
        # obj.first_name_new = p.first_name
        # obj.last_name_new = p.last_name

        # obj.first_name = obj.first_name_trans
        # obj.last_name = obj.last_name_trans
        # obj.save()
        # AttributeError: 'Person' object has no attribute 'first_name'
        # Even though it exists in the model

        p = PersonModel.objects.filter(id=obj.id).first()
        obj.first_name = p.first_name_trans
        obj.last_name = p.last_name_trans
        obj.save()


def backwards_func(apps, schema_editor):
    Person = apps.get_model('aldryn_people', 'Person')
    # PersonTranslation = apps.get_model('aldryn_people', 'PersonTranslation')

    for obj in Person.objects.all():
        # translation = _get_translation(obj, PersonTranslation)
        # obj.name = translation.name
        # obj.slug = translation.slug
        # obj.save()

        # obj.first_name = obj.first_name_new
        # obj.last_name = obj.last_name_new

        # p = PersonModel.objects.filter(id=obj.id).first()
        # obj.first_name = p.first_name_new
        # obj.last_name = p.last_name_new
        # django.db.utils.ProgrammingError: column aldryn_people_person.first_name does not exist

        # p = PersonModel.objects.filter(id=obj.id).first()
        # p.first_name = obj.first_name_new
        # p.last_name = obj.last_name_new
        # # django.db.utils.ProgrammingError: column aldryn_people_person.first_name does not exist
        #
        # # p = PersonModel.objects.filter(id=obj.id).first()
        # # p.translations.first_name = obj.first_name_new
        # # p.translations.last_name = obj.last_name_new
        # # django.db.utils.ProgrammingError: column aldryn_people_person.first_name does not exist
        # p.save()
        # # ACTUALLY; I realised I had actually deleted the field in models.py; so it actually didn't exist!

        # obj.first_name_trans = obj.first_name
        # obj.last_name_trans = obj.last_name
        # obj.save()
        # AttributeError: 'Person' object has no attribute 'first_name'
        # Even though it exists in the model


        p = PersonModel.objects.filter(id=obj.id).first()
        p.first_name_trans = obj.first_name
        p.last_name_trans = obj.last_name
        p.save()

# def _get_translation(object, MyModelTranslation):
#     translations = MyModelTranslation.objects.filter(master_id=object.pk)
#     try:
#         # Try default translation
#         return translations.get(language_code=settings.LANGUAGE_CODE)
#     except ObjectDoesNotExist:
#         try:
#             # Try default language
#             return translations.get(language_code=settings.PARLER_DEFAULT_LANGUAGE_CODE)
#         except ObjectDoesNotExist:
#             # Maybe the object was translated only in a specific language?
#             # Hope there is a single translation
#             return translations.get()




class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_people', '0038_add_name_fields'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]