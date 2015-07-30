# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_simpleslider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption_text',
            field=models.TextField(null=True, verbose_name='caption text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slider',
            name='image_options',
            field=models.ForeignKey(related_name='cmsplugin_simpleslider_image_options', on_delete=django.db.models.deletion.SET_NULL, verbose_name='image size', blank=True, to='cmsplugin_filer_image.ThumbnailOption', null=True),
            preserve_default=True,
        ),
    ]
