# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0001_initial'),
        ('cms', '0011_auto_20150419_1006'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('order', models.PositiveIntegerField(db_index=True, default=1, editable=False)),
                ('caption_text', models.CharField(max_length=255, verbose_name='caption text', blank=True, null=True)),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', related_name='image')),
            ],
            options={
                'verbose_name_plural': 'images',
                'abstract': False,
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, to='cms.CMSPlugin', parent_link=True, auto_created=True)),
                ('order', models.PositiveIntegerField(db_index=True, default=1, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='name', blank=True, null=True)),
                ('dots', models.BooleanField(verbose_name='dots', default=False)),
                ('fade', models.BooleanField(verbose_name='fade', default=False)),
                ('autoplay', models.BooleanField(verbose_name='autoplay', default=True)),
                ('image_options', models.ForeignKey(null=True, to='cmsplugin_filer_image.ThumbnailOption', on_delete=django.db.models.deletion.SET_NULL, related_name='djangocms_blog_post_thumbnail', verbose_name='image size', blank=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['order'],
            },
            bases=('cms.cmsplugin', models.Model),
        ),
        migrations.AddField(
            model_name='image',
            name='slider',
            field=models.ForeignKey(to='cmsplugin_simpleslider.Slider', related_name='images'),
            preserve_default=True,
        ),
    ]
