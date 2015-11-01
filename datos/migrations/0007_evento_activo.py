# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0006_auto_20151031_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
