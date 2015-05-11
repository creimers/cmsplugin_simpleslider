# -*- coding: utf-8 -*-

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.contrib import admin

from django.utils.translation import ugettext as _
from adminsortable.admin import SortableStackedInline
from adminsortable.admin import SortableAdmin

from .models import (
    Slider,
    Image
)


class ImageInline(SortableStackedInline):
    model = Image
    extra = 1


class SliderPlugin(CMSPluginBase, SortableAdmin):

    model = Slider
    name = _("Simple Slider")
    render_template = "cmsplugin_simpleslider/_slider.html"
    inlines = [ImageInline, ]

    def render(self, context, instance, placeholder):
        images = instance.slider.images.all()
        context.update({
            'images': images
        })

        context["dots"] = instance.dots
        context["fade"] = instance.fade
        context["autoplay"] = instance.autoplay

        return context

plugin_pool.register_plugin(SliderPlugin)
