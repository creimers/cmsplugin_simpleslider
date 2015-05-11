# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0001_initial'),
        ('cmsplugin_simpleslider', '0003_auto_20150511_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='image_options',
            field=models.ForeignKey(verbose_name='image size', to='cmsplugin_filer_image.ThumbnailOption', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='djangocms_blog_post_thumbnail'),
            preserve_default=True,
        ),
    ]
