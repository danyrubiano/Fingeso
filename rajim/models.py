from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

def url3(self, filename):
        ruta = "Artistas/%s/%s" % (self.nombre_artista, str(filename))
        return ruta

class Artista(models.Model):
    
    id_artista = models.AutoField(db_column='ID_ARTISTA', primary_key=True)  # Field name made lowercase.
    nombre_artista = models.CharField(db_column='NOMBRE_ARTISTA', max_length=60, blank=True, null=True)  # Field name made lowercase.
    resena = models.TextField(db_column='RESENA', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    fecha_nacimiento_artista = models.DateField(db_column='FECHA_NACIMIENTO_ARTISTA', blank=True, null=True)  # Field name made lowercase.
    valoracion_artista = models.IntegerField(db_column='VALORACION_ARTISTA', blank=True, null=True)  # Field name made lowercase.
    foto = models.ImageField(upload_to=url3)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.nombre_artista
        
    class Meta:
        managed = True
        db_table = 'artista'


    

class Cancion(models.Model):
    id_cancion = models.AutoField(db_column='ID_CANCION', primary_key=True)  # Field name made lowercase.
    id_disco = models.ForeignKey('Disco', db_column='ID_DISCO', blank=True, null=True)  # Field name made lowercase.
    nombre_cancion = models.CharField(db_column='NOMBRE_CANCION', max_length=60, blank=True, null=True)  # Field name made lowercase.
    duracion = models.IntegerField(db_column='DURACION', blank=True, null=True) # Field name made lowercase.
    val_cancion = models.IntegerField(db_column='VAL_CANCION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'cancion'

    def __str__(self):
        return self.nombre_cancion


class Compra(models.Model):
    id_compra = models.AutoField(db_column='ID_COMPRA', primary_key=True)  # Field name made lowercase.
    id_disco = models.ForeignKey('Disco', db_column='ID_DISCO', blank=True, null=True)  # Field name made lowercase.
    fecha_compra = models.DateTimeField(db_column='FECHA_COMPRA', blank=True, null=True)  # Field name made lowercase.
    precio_final = models.IntegerField(db_column='PRECIO_FINAL', blank=True, null=True)  # Field name made lowercase.
    tipo_pago = models.CharField(db_column='TIPO_PAGO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'compra'

def url(self, filename):
    ruta = "Discos/%s/%s" % (self.nombre_disco, str(filename))
    return ruta
    

class Disco(models.Model):


    id_disco = models.AutoField(db_column='ID_DISCO', primary_key=True)  # Field name made lowercase.
    id_artista = models.ForeignKey(Artista, db_column='ID_ARTISTA', blank=True,null=True)  # Field name made lowercase.
    id_compra = models.ForeignKey(Compra, db_column='ID_COMPRA', blank=True, null=True)  # Field name made lowercase.
    nombre_disco = models.CharField(db_column='NOMBRE_DISCO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fecha_lanzamiento = models.DateField(db_column='FECHA_LANZAMIENTO', blank=True, null=True)  # Field name made lowercase.
    genero = models.CharField(db_column='GENERO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    resena = models.TextField(db_column='RESENA', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    valoracion_disco = models.IntegerField(db_column='VALORACION_DISCO', blank=True, null=True)  # Field name made lowercase.
    precio = models.IntegerField(db_column='PRECIO', blank=True, null=True)  # Field name made lowercase.
    caratula = models.ImageField(upload_to=url)
    status = models.BooleanField(default=False)
    video = models.CharField(db_column='VIDEO', max_length=1024, blank=True, null=True)

    def __unicode__(self):
        return self.nombre_disco

    class Meta:
        managed = True
        db_table = 'disco'

    
def url2(self,filename):
    ruta = "Users/%s/%s"%(self.user.username,filename)
    return ruta


class userProfile(models.Model):

    user        =   models.OneToOneField(User, related_name="profile")
    photo       =   models.ImageField(upload_to=url2)
    fecha_nacimiento_user = models.DateField(db_column='FECHA_NACIMIENTO_USER',blank=True, null=True)  # Field name made lowercase.
    descuento = models.IntegerField(db_column='DESCUENTO', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    valoracion_user = models.IntegerField(db_column='VALORACION_USER', blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return self.user.username

class ComentaDisco(models.Model):

    id_cd = models.AutoField(db_column='ID_CD', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, db_column='ID_USER', unique=False , blank=True,null=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=40, blank=True, null=True)
    comentario = models.TextField(db_column='COMENTARIO', max_length=200, blank=True, null=True)
    id_disco = models.ForeignKey(Disco, db_column='ID_DISCO', unique=False, blank=True,null=True)  # Field name made lowercase.

    #agregar id_disco
class ValoraDisco(models.Model):

    id_vd = models.AutoField(db_column='ID_VD', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, db_column='ID_USER')
    id_disco = models.ForeignKey(Disco, db_column='ID_DISCO')  # Field name made lowercase.
    valoracion_disco = models.IntegerField(db_column='VALORACION_DISCO')

    class Meta:
        managed = True
        db_table = 'valoradisco'
        unique_together = (('user', 'id_disco'),)
