 # -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from rajim.models import *
from django.template import loader, Context, RequestContext
from .forms import *
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required
from django.core.mail.message import EmailMultiAlternatives
from django.http.response import HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage

# Create your views here.

def Artistas(request,id_artista):
    artista = Artista.objects.get(id_artista=id_artista)
    disco = Disco.objects.filter(id_artista=id_artista).order_by('id_disco')
    return render(request,'rajim/Artista.html',{'artista':artista, 'disco':disco},context_instance=RequestContext(request))

def BusquedaArtista(request):
    form = SearchForm()
    artistas = Artista.objects.filter(status=True)
    if request.method == "POST":
        form= SearchForm(request.POST)
        if form.is_valid():
            buscar = form.cleaned_data['buscar']
            artistass =Artista.objects.filter(nombre_artista__contains=buscar)
            return render(request,'rajim/BusquedaArtista2.html',{'form' :form,'artistass':artistass,'buscar' :buscar},context_instance=RequestContext(request))
    form = SearchForm()
    return render(request,'rajim/BusquedaArtista.html',{'form':form, 'artistas':artistas},context_instance=RequestContext(request))    

def Album(request,id_disco):
    user = request.user
    disco = Disco.objects.get(id_disco=id_disco)
    canciones = Cancion.objects.filter(id_disco=id_disco).order_by('id_cancion')
    form = ComentaDiscoForm()
    #form2 = ValoraDiscoForm()
    if request.method == "POST":
        form = ComentaDiscoForm(request.POST)
        #form2 = ValoraDiscoForm(request.POST)
        if form.is_valid:
            ComentaDisco = form.save(commit=False)
            #ValoraDisco = form.save(commit= False)
            ComentaDisco.user = user
            #ValoraDisco.user = user
            ComentaDisco.id_disco = disco
            #ValoraDiscoForm.id_disco = disco
            #valoracion = form2.cleaned_data['valoracion']
            #ValoraDisco.valoracion_disco= valoracion
            #ValoraDisco.save()
            ComentaDisco.save()
            #comentarios = ComentaDisco.objects.filter(id_disco=id_disco)

            return render(request,'rajim/Disco.html',{'disco':disco, 'canciones':canciones, 'form':form, 'comentarios':comentarios},context_instance=RequestContext(request))


             
    return render(request,'rajim/Disco.html',{'disco':disco, 'canciones':canciones, 'form':form},context_instance=RequestContext(request))


def BusquedaAlbum(request):
    form = SearchForm()
    discos = Disco.objects.filter(status=True)
    if request.method == "POST":
        form= SearchForm(request.POST)
        if form.is_valid():
            buscar = form.cleaned_data['buscar']
            discoss =Disco.objects.filter(nombre_disco__contains=buscar)
            return render(request,'rajim/BusquedaDisco2.html',{'form' :form,'discoss':discoss,'buscar' :buscar},context_instance=RequestContext(request))
    form = SearchForm()
    return render(request,'rajim/BusquedaDisco.html',{'form' :form,'discos':discos},context_instance=RequestContext(request))



def Contacto(request):
    user=request.user
    if request.method=='POST':
        form=Reporte(request.POST)
        if form.is_valid():
            user_form = UserForm(request.POST, instance=request.user)
            asunto = dict(CHOICES) [form.cleaned_data['Asunto']]
            nombre = user.username #user_form
            mensaje= form.cleaned_data['Mensaje']
            from_email =user.email #user_form
            
            
            #mail=EmailMessage(asunto,mensaje,from_email,to=['diego.jefecito@gmail.com'])
            #mail.send()
            
            html_content = "<h2>[%s] <br>Nombre:%s <br> Mensaje:%s"%(from_email,nombre,mensaje)
            msg = EmailMultiAlternatives(asunto, mensaje, from_email, to=['diego.jefecito@gmail.com'])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            #msg=EmailMultiAlternatives('Correo de Contacto',html_content,[to_admin])
            #msg.attach_alternative(html_content, "text/html")
            #msg.send()
        return HttpResponseRedirect('/')
    else:
        form=Reporte()
        
    return render_to_response('rajim/Contacto.html',{'form':form,}, context_instance=RequestContext(request))
		

def Registrar(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
        if request.method == "POST":
            form= RegisterForm(request.POST)
            if form.is_valid():
                usuario = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password_one = form.cleaned_data['password_one']
                password_two = form.cleaned_data['password_two']
                u = User.objects.create_user(username=usuario, email=email,password=password_one)
                u.save()
                perfil = userProfile(user=u, photo='\static\Fingeso\img\perfilphoto.jpg')
                perfil.save()
                return render(request,'rajim/Registrar2.html',context_instance=RequestContext(request))
            else:
                return render(request,'rajim/Registrar.html',{'form':form},context_instance=RequestContext(request))

        return render(request,'rajim/Registrar.html',{'form':form},context_instance=RequestContext(request))

def Ingresar(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/')
                else:
                    mensaje = "usuario y/o password incorrecto"
        form = LoginForm()
        return render(request,'rajim/Ingresar.html',{'form':form, 'mensaje':mensaje},context_instance=RequestContext(request))

def CerrarSesion(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def Ranking(request):
    rankartista = Artista.objects.filter(valoracion_artista__isnull=False).order_by('-valoracion_artista')
    rankdisco = Disco.objects.filter(valoracion_disco__isnull=False).order_by('-valoracion_disco')
    rankuser = userProfile.objects.filter(valoracion_user__isnull=False).order_by('-valoracion_user')
    return render(request,'rajim/Ranking.html',{ 'rankdisco':rankdisco,'rankartista':rankartista ,'rankuser':rankuser})
def Registrar2(request):
    return render(request, 'rajim/Registrar2.html',{})
def Perfil(request):
    if request.user.is_authenticated():
        return render(request, 'rajim/Perfil.html',{})

    else:
        return HttpResponseRedirect('/')

    return render(request, 'rajim/Perfil.html',{})

def EditarPerfil(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            # formulario enviado
            user_form = UserForm(request.POST, instance=request.user)
            perfil_form = PerfilForm(request.POST, request.FILES, instance=request.user.profile)
            if user_form.is_valid() and perfil_form.is_valid():
                # formulario validado correctamente
                user_form.save()
                perfil_form.save()

            return HttpResponseRedirect('/rajim/Perfil.html')

        else:
            # formulario inicial
            user_form = UserForm(instance=request.user)
            perfil_form = PerfilForm(instance=request.user.profile)
        return render(request,'rajim/EditarPerfil.html', { 'user_form': user_form,  'perfil_form': perfil_form }, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')





