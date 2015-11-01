# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0007_evento_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='slug',
            field=models.SlugField(max_length=128, verbose_name=b'slug', blank=True),
        ),
    ]
