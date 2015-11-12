# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0009_auto_20151107_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='politico',
            name='partido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='datos.Partido', null=True),
        ),
    ]
