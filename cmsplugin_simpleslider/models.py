from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from filer.fields.image import FilerImageField

from adminsortable.models import Sortable


@python_2_unicode_compatible
class Slider(CMSPlugin, Sortable):
    class Meta(Sortable.Meta):
        pass

    name = models.CharField(_('name'), max_length=50, blank=True, null=True)
    dots = models.BooleanField(_('dots'), default=False)
    fade = models.BooleanField(_('fade'), default=False)
    autoplay = models.BooleanField(_('autoplay'), default=True)

    def copy_relations(self, oldinstance):
        for image in oldinstance.images.all():
            image.pk = None
            image.slider = self
            image.save()

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.pk


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
