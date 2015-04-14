# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '__first__'),
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption_text', models.CharField(max_length=255, null=True, blank=True, verbose_name='caption text')),
                ('image', filer.fields.image.FilerImageField(related_name='image', to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, primary_key=True, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=50, null=True, blank=True, verbose_name='name')),
                ('dots', models.BooleanField(default=False, verbose_name='dots')),
                ('fade', models.BooleanField(default=False, verbose_name='fade')),
                ('autoplay', models.BooleanField(default=True, verbose_name='autoplay')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='image',
            name='slider',
            field=models.ForeignKey(related_name='images', to='simple_slider.Slider'),
            preserve_default=True,
        ),
    ]
