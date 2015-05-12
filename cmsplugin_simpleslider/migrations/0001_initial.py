# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150511_1555'),
        ('cms', '0011_auto_20150419_1006'),
        ('cmsplugin_filer_image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('order', models.PositiveIntegerField(db_index=True, default=1, editable=False)),
                ('caption_text', models.CharField(max_length=255, verbose_name='caption text', null=True, blank=True)),
                ('image', filer.fields.image.FilerImageField(related_name='image', to='filer.Image')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'images',
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, serialize=False, to='cms.CMSPlugin', primary_key=True, parent_link=True)),
                ('order', models.PositiveIntegerField(db_index=True, default=1, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='name', null=True, blank=True)),
                ('dots', models.BooleanField(verbose_name='dots', default=False)),
                ('fade', models.BooleanField(verbose_name='fade', default=False)),
                ('autoplay', models.BooleanField(verbose_name='autoplay', default=True)),
                ('image_options', models.ForeignKey(verbose_name='image size', null=True, to='cmsplugin_filer_image.ThumbnailOption', related_name='djangocms_blog_post_thumbnail', blank=True, on_delete=django.db.models.deletion.SET_NULL)),
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
            field=models.ForeignKey(related_name='images', to='cmsplugin_simpleslider.Slider'),
            preserve_default=True,
        ),
    ]
