# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rajim', '0003_auto_20150616_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentaDisco',
            fields=[
                ('id_cd', models.AutoField(serialize=False, primary_key=True, db_column='ID_CD')),
                ('titulo', models.CharField(max_length=40, null=True, db_column='TITULO', blank=True)),
                ('comentario', models.TextField(max_length=200, null=True, db_column='COMENTARIO', blank=True)),
                ('user', models.ForeignKey(db_column='ID_USER', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ValoraDisco',
            fields=[
                ('id_vd', models.AutoField(serialize=False, primary_key=True, db_column='ID_VD')),
                ('valoracion_disco', models.IntegerField(db_column='VALORACION_DISCO')),
                ('id_disco', models.ForeignKey(to='rajim.Disco', db_column='ID_DISCO')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column='ID_USER')),
            ],
            options={
                'db_table': 'valoradisco',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='valoradisco',
            unique_together=set([('user', 'id_disco')]),
        ),
    ]
