# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import rajim.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id_artista', models.AutoField(serialize=False, primary_key=True, db_column='ID_ARTISTA')),
                ('nombre_artista', models.CharField(max_length=60, null=True, db_column='NOMBRE_ARTISTA', blank=True)),
                ('resena', models.TextField(max_length=1024, null=True, db_column='RESENA', blank=True)),
                ('fecha_nacimiento_artista', models.DateField(null=True, db_column='FECHA_NACIMIENTO_ARTISTA', blank=True)),
                ('valoracion_artista', models.IntegerField(null=True, db_column='VALORACION_ARTISTA', blank=True)),
            ],
            options={
                'db_table': 'artista',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id_cancion', models.AutoField(serialize=False, primary_key=True, db_column='ID_CANCION')),
                ('nombre_cancion', models.CharField(max_length=60, null=True, db_column='NOMBRE_CANCION', blank=True)),
                ('duracion', models.IntegerField(null=True, db_column='DURACION', blank=True)),
                ('val_cancion', models.IntegerField(null=True, db_column='VAL_CANCION', blank=True)),
            ],
            options={
                'db_table': 'cancion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_compra', models.AutoField(serialize=False, primary_key=True, db_column='ID_COMPRA')),
                ('fecha_compra', models.DateTimeField(null=True, db_column='FECHA_COMPRA', blank=True)),
                ('precio_final', models.IntegerField(null=True, db_column='PRECIO_FINAL', blank=True)),
                ('tipo_pago', models.CharField(max_length=10, null=True, db_column='TIPO_PAGO', blank=True)),
            ],
            options={
                'db_table': 'compra',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('id_disco', models.AutoField(serialize=False, primary_key=True, db_column='ID_DISCO')),
                ('nombre_disco', models.CharField(max_length=60, null=True, db_column='NOMBRE_DISCO', blank=True)),
                ('fecha_lanzamiento', models.DateField(null=True, db_column='FECHA_LANZAMIENTO', blank=True)),
                ('genero', models.CharField(max_length=100, null=True, db_column='GENERO', blank=True)),
                ('resena', models.TextField(max_length=1024, null=True, db_column='RESENA', blank=True)),
                ('valoracion_disco', models.IntegerField(null=True, db_column='VALORACION_DISCO', blank=True)),
                ('precio', models.IntegerField(null=True, db_column='PRECIO', blank=True)),
                ('caratula', models.ImageField(upload_to=rajim.models.url)),
                ('status', models.BooleanField(default=False)),
                ('id_artista', models.ForeignKey(db_column='ID_ARTISTA', blank=True, to='rajim.Artista', null=True)),
                ('id_compra', models.ForeignKey(db_column='ID_COMPRA', blank=True, to='rajim.Compra', null=True)),
            ],
            options={
                'db_table': 'disco',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=rajim.models.url2)),
                ('fecha_nacimiento_user', models.DateField(null=True, db_column='FECHA_NACIMIENTO_USER', blank=True)),
                ('descuento', models.IntegerField(null=True, db_column='DESCUENTO', blank=True)),
                ('direccion', models.CharField(max_length=40, null=True, db_column='DIRECCION', blank=True)),
                ('valoracion_user', models.IntegerField(null=True, db_column='VALORACION_USER', blank=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='id_disco',
            field=models.ForeignKey(db_column='ID_DISCO', blank=True, to='rajim.Disco', null=True),
        ),
        migrations.AddField(
            model_name='cancion',
            name='id_disco',
            field=models.ForeignKey(db_column='ID_DISCO', blank=True, to='rajim.Disco', null=True),
        ),
    ]
