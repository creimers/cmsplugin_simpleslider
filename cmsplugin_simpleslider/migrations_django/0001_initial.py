# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
        ('cmsplugin_filer_image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('caption_text', models.CharField(blank=True, verbose_name='caption text', max_length=255, null=True)),
                ('image', filer.fields.image.FilerImageField(related_name='image', to='filer.Image')),
            ],
            options={
                'abstract': False,
                'ordering': ['order'],
                'verbose_name_plural': 'images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', auto_created=True, parent_link=True, primary_key=True, serialize=False)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('name', models.CharField(blank=True, verbose_name='name', max_length=50, null=True)),
                ('dots', models.BooleanField(default=False, verbose_name='dots')),
                ('fade', models.BooleanField(default=False, verbose_name='fade')),
                ('autoplay', models.BooleanField(default=True, verbose_name='autoplay')),
                ('image_options', models.ForeignKey(verbose_name='image size', blank=True, null=True, related_name='djangocms_blog_post_thumbnail', on_delete=django.db.models.deletion.SET_NULL, to='cmsplugin_filer_image.ThumbnailOption')),
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
