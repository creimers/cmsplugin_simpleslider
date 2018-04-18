#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
gettext = lambda s: s

HELPER_SETTINGS = {
    'NOSE_ARGS': [
        '-s',
    ],
    'INSTALLED_APPS': [
        'filer',
        'easy_thumbnails',
        'adminsortable',
        'cmsplugin_filer_image',
        'cmsplugin_simpleslider',
    ],
    'LANGUAGE_CODE': 'en',
    'LANGUAGES': (
        ('en', gettext('en')),
    ),
    'CMS_LANGUAGES': {
        ## Customize this
        1: [
            {
                'redirect_on_fallback': True,
                'hide_untranslated': False,
                'name': gettext('en'),
                'code': 'en',
                'public': True,
            },
        ],
        'default': {
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    },
    'MIDDLEWARE_CLASSES': [
        'django.contrib.messages.middleware.MessageMiddleware',
    ],
    #  'TEMPLATE_CONTEXT_PROCESSORS': {
        #  'django.core.context_processors.static'
    #  },
    'THUMBNAIL_PROCESSORS': (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    )
}
