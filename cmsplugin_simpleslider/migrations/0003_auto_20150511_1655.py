# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_simpleslider', '0002_auto_20150511_1638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='slider',
            name='order',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=True,
        ),
    ]
