# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0011_auto_20151113_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='politico',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'politicos', blank=True),
        ),
    ]
