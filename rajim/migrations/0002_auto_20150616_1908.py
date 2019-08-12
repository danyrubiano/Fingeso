# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import rajim.models


class Migration(migrations.Migration):

    dependencies = [
        ('rajim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='foto',
            field=models.ImageField(default='', upload_to=rajim.models.url3),
        ),
        migrations.AddField(
            model_name='artista',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='disco',
            name='video',
            field=models.CharField(max_length=1024, null=True, db_column='VIDEO', blank=True),
        ),
    ]
