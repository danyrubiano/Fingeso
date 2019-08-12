from django.conf.urls import patterns, include, url
from django.contrib import admin
from rajim import views

urlpatterns = [
    url(r'^Disco/(?P<id_disco>.*)/$', views.Album),
    url(r'^BusquedaDisco.html$', views.BusquedaAlbum),
    url(r'^Contacto.html$', views.Contacto),
    url(r'^Registrar.html$', views.Registrar),
    url(r'^Ingresar.html$', views.Ingresar),
    url(r'^Ranking.html$', views.Ranking),
    url(r'^Registrar2.html$', views.Registrar2),
    url(r'^CerrarSesion.html$', views.CerrarSesion),
    url(r'^Perfil.html$', views.Perfil),
    url(r'^EditarPerfil.html$', views.EditarPerfil),
    url(r'^Artista/(?P<id_artista>.*)/$', views.Artistas),
    url(r'^BusquedaArtista.html$', views.BusquedaArtista),




]
