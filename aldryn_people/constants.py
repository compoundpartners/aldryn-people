# -*- coding: utf-8 -*-

from django.conf import settings

UPDATE_SEARCH_DATA_ON_SAVE = getattr(
    settings,
    'PEOPLE_UPDATE_SEARCH_DATA_ON_SAVE',
    False,
)

PEOPLE_PLUGIN_STYLES = getattr(
    settings,
    'PEOPLE_PLUGIN_STYLES',
    '',
)

ALDRYN_PEOPLE_USER_THRESHOLD = getattr(
    settings,
    'ALDRYN_PEOPLE_USER_THRESHOLD',
    50,
)

ALDRYN_PEOPLE_HIDE_SUFFIX = getattr(
    settings,
    'ALDRYN_PEOPLE_HIDE_SUFFIX',
    0,
)
ALDRYN_PEOPLE_HIDE_FAX = getattr(
    settings,
    'ALDRYN_PEOPLE_HIDE_FAX',
    0,
)
ALDRYN_PEOPLE_HIDE_WEBSITE = getattr(
    settings,
    'ALDRYN_PEOPLE_HIDE_WEBSITE',
    0,
)
ALDRYN_PEOPLE_HIDE_FACEBOOK = getattr(
    settings,
    'ALDRYN_PEOPLE_HIDE_FACEBOOK',
    0,
)
ALDRYN_PEOPLE_HIDE_TWITTER = getattr(
    settings,
    'ALDRYN_PEOPLE_HIDE_TWITTER',
    0,
)
ALDRYN_PEOPLE_HIDE_LINKEDIN = getattr(
    settings,
    'ALDRYN_PEOPLE_HIDE_LINKEDIN',
    0,
)
ALDRYN_PEOPLE_HIDE_GROUPS = getattr(
    settings,
    'ALDRYN_PEOPLE_HIDE_GROUPS',
    0,
)
ALDRYN_PEOPLE_HIDE_LOCATION = getattr(
    settings,
    'ALDRYN_PEOPLE_HIDE_LOCATION',
    0,
)
ALDRYN_PEOPLE_HIDE_USER = getattr(
    settings,
    'ALDRYN_PEOPLE_HIDE_USER',
    0,
)
ALDRYN_PEOPLE_SHOW_SECONDARY_IMAGE = getattr(
    settings,
    'ALDRYN_PEOPLE_SHOW_SECONDARY_IMAGE',
    0,
)
ALDRYN_PEOPLE_SHOW_SECONDARY_PHONE = getattr(
    settings,
    'ALDRYN_PEOPLE_SHOW_SECONDARY_PHONE',
    0,
)
ALDRYN_PEOPLE_SUMMARY_RICHTEXT = getattr(
    settings,
    'ALDRYN_PEOPLE_SUMMARY_RICHTEXT',
    0,
)
ADD_FILTERED_CATEGORIES = getattr(
    settings,
    'ALDRYN_PEOPLE_ADD_FILTERED_CATEGORIES',
    [],
)
ADDITIONAL_EXCLUDE = getattr(
    settings,
    'ALDRYN_PEOPLE_ADDITIONAL_EXCLUDE',
    {},
)
SHOW_GROUP_LIST_VIEW = getattr(
    settings,
    'ALDRYN_PEOPLE_SHOW_GROUP_LIST_VIEW',
    True,
)
URL_PREFIX = getattr(
    settings,
    'ALDRYN_PEOPLE_URL_PREFIX',
    '',
)
INDEX_GROUP_LIST = getattr(
    settings,
    'ALDRYN_PEOPLE_INDEX_GROUP_LIST',
    [],
)
INDEX_DEFAULT_FILTERS = getattr(
    settings,
    'ALDRYN_PEOPLE_INDEX_DEFAULT_FILTERS',
    {},
)
DEFAULT_SORTING = getattr(
    settings,
    'ALDRYN_PEOPLE_DEFAULT_SORTING',
    ('last_name',),
)
SITEMAP_CHANGEFREQ = getattr(
    settings,
    'ALDRYN_PEOPLE_SITEMAP_CHANGEFREQ',
    'monthly',
)
SITEMAP_PRIORITY = getattr(
    settings,
    'ALDRYN_PEOPLE_SITEMAP_PRIORITY',
    0.5,
)
try:
    IS_THERE_COMPANIES = True
    from js_companies.models import Company
except:
    IS_THERE_COMPANIES = False
