# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0010_auto_20151112_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='BitacoraPartidoPolitico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='datos.Partido', null=True)),
                ('politico', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='datos.Politico', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
        ),
    ]
