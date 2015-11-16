# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0012_politico_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ('-creacion',)},
        ),
    ]
