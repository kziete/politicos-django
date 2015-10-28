# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
        ('datos', '0002_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='autor',
            field=models.ForeignKey(default=1, to='sitio.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='fuente',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
