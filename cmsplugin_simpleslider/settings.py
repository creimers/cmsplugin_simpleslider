# -*- coding: utf-8 -*-
from django.conf import settings

def get_settings(name):
    default = {
        'SLIDER_IMAGE_OPTIONS': getattr(settings, 'SLIDER_IMAGE_OPTIONS', {
            'size': '1000x500',
            'crop': True,
            'upscale': True
        }),
    }
    return default[name]
