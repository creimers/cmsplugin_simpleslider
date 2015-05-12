from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User

from django.core.files.uploadedfile import SimpleUploadedFile
from filer.models import Image
from cmsplugin_filer_image.models import ThumbnailOption

from cms import api
from cms.models import CMSPlugin
from cms.test_utils.testcases import BaseCMSTestCase
from cms.utils import get_cms_setting

from . import models
from . import cms_plugins


class SimpleSliderTestCase(TestCase, BaseCMSTestCase):
    su_username = 'user'
    su_password = 'pass'

    def setUp(self):
        self.template = get_cms_setting('TEMPLATES')[0][0]
        self.language = settings.LANGUAGES[0][0]
        self.page = api.create_page('page', self.template, self.language, published=True)
        self.placeholder = self.page.placeholders.all()[0]
        self.superuser = self.create_superuser()

    def tearDown(self):
        self.client.logout()

    def create_superuser(self):
        return User.objects.create_superuser(self.su_username, 'email@example.com', self.su_password)

    def test_add_slider_plugin(self):
        slider_plugin = api.add_plugin(
            self.placeholder,
            cms_plugins.SliderPlugin,
            self.language,
            name='affe'
        )

        image_options = ThumbnailOption.objects.create(
            name='base', width=100, height=100, crop=True, upscale=False
        )
        slider_plugin.image_options = image_options

        image_file = SimpleUploadedFile(
            'affe.jpg', b'affe', content_type="image/jpeg")
        img1 = Image.objects.create(
            owner=self.superuser, original_filename='affe.jpg', file=image_file
        )
        img2 = Image.objects.create(
            owner=self.superuser, original_filename='affe2.jpg', file=image_file
        )
        image1 = models.Image(image=img1)
        image1.slider = slider_plugin
        image1.save()

        self.assertTrue(image1.__str__() == 'affe.jpg')

        image2 = models.Image(image=img2)
        image2.slider = slider_plugin
        image2.save()

        self.assertTrue(image2.__str__() == 'affe2.jpg')

        self.assertTrue(slider_plugin.__str__() == 'affe')
        self.assertTrue(
            models.Slider.objects.filter(pk=slider_plugin.pk).exists()
        )
        self.assertTrue(
            len(models.Slider.objects.filter(pk=slider_plugin.pk).first().images.all()), 2
        )

    def test_render_page(self):
        self.test_add_slider_plugin()
        api.publish_page(self.page, self.superuser, self.language)
        response = self.client.get(self.page.get_absolute_url())

        self.assertTrue("slider-wrapper" in response.rendered_content)
        self.assertTrue("single-image" in response.rendered_content)
