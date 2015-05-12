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
        'cmsplugin_filer_image',
        'adminsortable',
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
                'code': 'de',
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
    'MIGRATION_MODULES': {
        'filer': 'filer.migrations_django',
        'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
        'cmsplugin_simpleslider': 'cmsplugin_simpleslider.migrations_django',
    },
}
