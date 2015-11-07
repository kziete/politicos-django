# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0008_evento_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(max_length=128, verbose_name=b'T\xc3\xadtulo'),
        ),
    ]
