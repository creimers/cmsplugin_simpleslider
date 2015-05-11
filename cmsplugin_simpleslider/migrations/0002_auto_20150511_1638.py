# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_simpleslider', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name_plural': 'images', 'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=True,
        ),
    ]
