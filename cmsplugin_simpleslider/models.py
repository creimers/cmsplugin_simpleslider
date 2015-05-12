# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from filer.fields.image import FilerImageField

from cmsplugin_filer_image.models import ThumbnailOption

from adminsortable.models import Sortable

from .settings import get_settings


@python_2_unicode_compatible
class Slider(CMSPlugin, Sortable):
    class Meta(Sortable.Meta):
        pass

    name = models.CharField(_('name'), max_length=50, blank=True, null=True)
    dots = models.BooleanField(_('dots'), default=False)
    fade = models.BooleanField(_('fade'), default=False)
    autoplay = models.BooleanField(_('autoplay'), default=True)
    image_options = models.ForeignKey(
        ThumbnailOption,
        verbose_name=_('image size'),
        related_name='cmsplugin_simpleslider_image_options',
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def copy_relations(self, oldinstance):
        for image in oldinstance.images.all():
            image.pk = None
            image.slider = self
            image.save()

    def get_image_options(self):
        if self.image_options_id:
            return self.image_options.as_dict
        else:
            return get_settings('SLIDER_IMAGE_OPTIONS')

    def __str__(self):
        if self.name:
            return self.name
        else:
            return 'sortable slider'


@python_2_unicode_compatible
class Image(Sortable):

    class Meta(Sortable.Meta):
        verbose_name_plural = _('images')
        pass

    slider = models.ForeignKey(
        Slider,
        related_name="images"
    )

    image = FilerImageField(
        related_name=_('image'),
    )

    caption_text = models.CharField(
        _('caption text'),
        null=True,
        blank=True,
        max_length=255
    )

    def __str__(self):
        if self.caption_text:
            return self.caption_text
        else:
            return self.image.label
