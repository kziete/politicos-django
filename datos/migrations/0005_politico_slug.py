# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0004_campana_politicocampana'),
    ]

    operations = [
        migrations.AddField(
            model_name='politico',
            name='slug',
            field=models.SlugField(max_length=60, verbose_name=b'slug', blank=True),
        ),
    ]
