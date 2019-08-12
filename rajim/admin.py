from django.contrib import admin
from .models import *
# Register your models here.

#class UsuarioAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['nombre_user','email_user','direccion','descuento']})
#    ]
#    list_display = ('nombre_user', 'email_user')
class ArtistaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nombre_artista']}),
        (None, {'fields': ['fecha_nacimiento_artista']}),
        (None, {'fields': ['foto','status']}),
        (None, {'fields': ['valoracion_artista']}),

        ('Descripcion', {'fields': ['resena']}),
        
    ]
    list_display = ('nombre_artista', 'fecha_nacimiento_artista')
class CancionEnlinea(admin.TabularInline):
    model = Cancion
    fields = ['nombre_cancion','duracion']
    extra = 3
class DiscoAdmin(admin.ModelAdmin):
    fields = ['id_artista','nombre_disco','fecha_lanzamiento','genero','precio','valoracion_disco','caratula','status','resena','video']
    inlines = [CancionEnlinea]
    list_display = ('nombre_disco','fecha_lanzamiento','genero','precio')

class ComentaDiscoAdmin(admin.ModelAdmin):
    list_display=('id_disco','user','titulo')

class ValoraDiscoAdmin(admin.ModelAdmin):
    list_display=('id_disco','user','valoracion_disco')

admin.site.register(userProfile)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Disco, DiscoAdmin)
admin.site.register(Cancion)
admin.site.register(ComentaDisco,ComentaDiscoAdmin)
admin.site.register(ValoraDisco,ValoraDiscoAdmin)





