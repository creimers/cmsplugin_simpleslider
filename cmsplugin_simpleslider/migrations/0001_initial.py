# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('cms', '0003_auto_20140926_2347'),
        ('cmsplugin_filer_image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('caption_text', models.CharField(max_length=255, null=True, verbose_name='caption text', blank=True)),
                ('image', filer.fields.image.FilerImageField(related_name='Bild', to='filer.Image')),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
                'verbose_name_plural': 'images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name='name', blank=True)),
                ('dots', models.BooleanField(default=False, verbose_name='dots')),
                ('fade', models.BooleanField(default=False, verbose_name='fade')),
                ('autoplay', models.BooleanField(default=True, verbose_name='autoplay')),
                ('image_options', models.ForeignKey(related_name='djangocms_blog_post_thumbnail', on_delete=django.db.models.deletion.SET_NULL, verbose_name='image size', blank=True, to='cmsplugin_filer_image.ThumbnailOption', null=True)),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
            bases=('cms.cmsplugin', models.Model),
        ),
        migrations.AddField(
            model_name='image',
            name='slider',
            field=models.ForeignKey(related_name='images', to='cmsplugin_simpleslider.Slider'),
            preserve_default=True,
        ),
    ]
