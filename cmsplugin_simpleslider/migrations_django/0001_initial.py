# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('filer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('caption_text', models.CharField(null=True, blank=True, verbose_name='caption text', max_length=255)),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', related_name='image')),
            ],
            options={
                'verbose_name_plural': 'images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', serialize=False, primary_key=True, auto_created=True, parent_link=True)),
                ('name', models.CharField(null=True, blank=True, verbose_name='name', max_length=50)),
                ('dots', models.BooleanField(verbose_name='dots', default=False)),
                ('fade', models.BooleanField(verbose_name='fade', default=False)),
                ('autoplay', models.BooleanField(verbose_name='autoplay', default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='image',
            name='slider',
            field=models.ForeignKey(to='cmsplugin_simpleslider.Slider', related_name='images'),
            preserve_default=True,
        ),
    ]
