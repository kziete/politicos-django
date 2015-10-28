# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0003_auto_20151028_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PoliticoCampana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campana', models.ForeignKey(to='datos.Campana')),
                ('politico', models.ForeignKey(to='datos.Politico')),
            ],
        ),
    ]
