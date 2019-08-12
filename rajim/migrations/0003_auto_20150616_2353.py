# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import rajim.models


class Migration(migrations.Migration):

    dependencies = [
        ('rajim', '0002_auto_20150616_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='foto',
            field=models.ImageField(upload_to=rajim.models.url3),
        ),
    ]
