# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0005_politico_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='creacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 1, 1, 33, 14, 372199, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 1, 1, 33, 25, 354046, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
