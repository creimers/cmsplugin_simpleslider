# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150511_1555'),
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('caption_text', models.CharField(verbose_name='caption text', blank=True, null=True, max_length=255)),
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
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='cms.CMSPlugin', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='name', blank=True, null=True, max_length=50)),
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
            field=models.ForeignKey(related_name='images', to='cmsplugin_simpleslider.Slider'),
            preserve_default=True,
        ),
    ]
