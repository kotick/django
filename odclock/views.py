# -*- encoding: utf-8 -*-
 
##
# App: app
##
 
# Core
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
 
# Forms
from forms import *
 
# Decorators
from django.contrib.auth.decorators import login_required
 
# Messages, Login, Logout and User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
 
# Models
from odclock.models import *
 
# JSON
from django.utils import simplejson
from django.utils.safestring import SafeString
 
# Data Structures
from django.utils.datastructures import SortedDict
 
# CACHE
from django.core.cache import cache
 
# CSV output
from django.template import loader, Context


def index(request):
    title = 'Clinica Odontologica'
    return render_to_response(
        
        'index.html',
        {
            'title': title,
        },
        context_instance=RequestContext(request)
    )

def ubicacion(request):    
    title = 'Clinica Odontologica'
    return render_to_response(
        
        'ubicacion.html',
        {
            'title': title,
        },
        context_instance=RequestContext(request)
    )

def tomahora(request):    
    title = 'Clinica Odontologica'    
    login_form = LoginForm()
    regis_form = RegisForm()
    return render_to_response(        
        'tomahora.html',
        {
            'title': title,            
            'login_form': login_form,
            'regis_form': regis_form
        },
        context_instance=RequestContext(request)
    )

def quienessomos(request):    
    title = 'Clinica Odontologica'
    return render_to_response(
        'quienessomos.html',
        {
            'title': title,
        },
        context_instance=RequestContext(request)
    )
    
def seccionpersonal(request):    
    title = 'Clinica Odontologica'
    login_form = LoginForm()
    return render_to_response(        
        'seccionpersonal.html',
        {
            'title': title,
            'login_form': login_form,
        },
        context_instance=RequestContext(request)
    )

def login_view(request):
    """
    Vista encargada autenticar un usuario para ingresar al sistema
    """
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # redireccionar al inicio
                return HttpResponseRedirect('/')
            else:
                # warning
                #messages.warning(request, 'Tu cuenta ha sido desactivada.')
                #return HttpResponseRedirect('/')
                return HttpResponse('<h1>ERROR desactivada</h1>')
        else:
            # error
            #messages.error(request, 'Nombre de usuario o contraseña errónea.')
            #return HttpResponseRedirect('/')
            return HttpResponse('<h1>ERROR no existe</h1>')
    else:
        return HttpResponseRedirect('/')

def crear_usuario(request):
    url = '/'
    if not request.user.is_anonymous():
        messages.error(request, 'ERROR no es anonimo')
        return HttpResponseRedirect(url)

    if not request.method == 'POST':
        messages.error(request, 'ERROR no es post')
        return HttpResponseRedirect(url)

    form = LoginForm(request.POST)
    
    # El formulario debe ser válido
    if not form.is_valid():
        messages.error(request, 'Formulario Malo')
        return HttpResponseRedirect(url)

    # ----- Valido

    if 'password1' != 'password2':
        messages.error(request, 'las dos claves deben ser correctas')
        #return HttpResponseRedirect(url)

    new_user = User(username=username, password=password1)
    new_user.save()

    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')