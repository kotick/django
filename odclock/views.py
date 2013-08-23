# -*- encoding: utf-8 -*-

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


def oli(request):
    title='Clinica Odontologica'
    return render_to_response(
        'oli.html',
        {
            'title':title,
        },
        context_instance=RequestContext(request)



        )


    


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

@login_required
def paciente(request):    
    title = 'Clinica Odontologica'
    usuario = User.objects.get(username=request.user)

    if request.user.first_name =='Dentista':
        return HttpResponseRedirect('/')

    if request.user.first_name =='Secretaria':
        return HttpResponseRedirect('/')

    if Paciente.objects.filter(user=usuario):
        agendamientos = Agendamiento.objects.filter(paciente= usuario.paciente)
        modificarp_form = ModificarP()
        modificare_form = ModificarE()
        modificartc_form = ModificarTc()
        modificartf_form = ModificarTf()
        verhorarioe_form=VerhorariosE()
        verhorariod_form=VerhorariosD()
        error = False
        return render_to_response(        
            'paciente.html',
            {
                'title': title,
                'agendamientos': agendamientos,
                'modificarp_form':modificarp_form,
                'modificare_form':modificare_form,
                'modificartc_form':modificartc_form,
                'modificartf_form':modificartf_form,
                'verhorarioe_form':verhorarioe_form,
                'verhorariod_form':verhorariod_form,
                'error':error,
            },
            context_instance=RequestContext(request)
        )
    else:
        return HttpResponseRedirect('/sesionpaciente')

def iniciosesionpaciente(request):
    title = 'Clinica Odontologica'    
    login_form = LoginForm()
    regis_form = RegisForm()
    return render_to_response(        
        'iniciosesionpaciente.html',
        {
            'title': title,            
            'login_form': login_form,
            'regis_form': regis_form,
        },
        context_instance=RequestContext(request)
    )
def iniciosesionpersonal(request):
    title = 'Clinica Odontologica'
    login_form = LoginForm()
    return render_to_response(        
        'iniciosesionpersonal.html',
        {
            'title': title,
            'login_form': login_form,
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

@login_required
def dentista(request):
    title = 'Clinica Odontologica'
    usuario = User.objects.get(username=request.user)
    agendamientos=Agendamiento.objects.filter(dentista=usuario.dentista)
    verficha_form=Verficha()
    atencion_form=IngresarAtencion()
    modificarp_form = ModificarP()
    modificare_form = ModificarE()
    modificartc_form = ModificarTc()
    modificartf_form = ModificarTf()
    return render_to_response(
        'dentista.html',
        {
            'title': title,
            'atencion_form':atencion_form,
            'agendamientos':agendamientos,
            'verficha_form':verficha_form,
            'modificarp_form':modificarp_form,
            'modificare_form':modificare_form,
            'modificartc_form':modificartc_form,
            'modificartf_form':modificartf_form,
        },
        context_instance=RequestContext(request)
    )

@login_required
def secretaria(request):    
    title = 'Clinica Odontologica'
    return render_to_response(
        'secretaria.html',
        {
            'title': title,
        },
        context_instance=RequestContext(request)
    )
    
   
@login_required 
def administrador(request):
    Adentista_form=AgregarDentista()
    Edentista_form=EliminarDentista()
    Ingresar_form=IngresarOferta()
    Borrar_form=BorrarOferta()
    Asignar_form=AsignarEspecialidad()
    Desasignar_form=DesasignarEspecialidad()
    Aespecialidad_form=AgregarEspecialidad()
    Eespecialidad_form=EliminarEspecialidad()
    Abox_form=AgregarBox()
    Ebox_form=EliminarBox()
    Asecretaria_form=AgregarSecretaria()
    Esecretaria_form=EliminarSecretaria()

    if request.user.first_name =='Dentista':
        if request.user.last_name !='Administrador':
            return HttpResponseRedirect('/dentista')
    if request.user.first_name =='Secretaria':
        if request.user.last_name !='Administrador':
            return HttpResponseRedirect('/secretaria')    
    if request.user.first_name =='Paciente':
        return HttpResponseRedirect('/')

    else:
          
        title = 'Clinica Odontologica'
        login_form = LoginForm()
        return render_to_response(        
            'administrador.html',
            {
                'title': title,
                'Adentista_form':Adentista_form,
                'Edentista_form':Edentista_form,
                'Ingresar_form':Ingresar_form,
                'Borrar_form':Borrar_form,
                'Asignar_form':Asignar_form,
                'Aespecialidad_form':Aespecialidad_form,
                'Eespecialidad_form':Eespecialidad_form,
                'Abox_form':Abox_form,
                'Ebox_form':Ebox_form,
                'Asecretaria_form':Asecretaria_form,
                'Esecretaria_form':Esecretaria_form,
                'Desasignar_form':Desasignar_form,

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
                usuario = User.objects.get(username=user)
                if usuario.first_name =='Paciente':
                    if usuario.paciente.desabilitado:
                        logout(request)
                        return HttpResponseRedirect('/')
                    else:
                        return HttpResponseRedirect('/paciente')
                else:
                    if usuario.first_name =='Dentista':
                        if usuario.dentista.desabilitado:
                            logout(request)
                            return HttpResponseRedirect('/')
                        else:
                            return HttpResponseRedirect('/dentista')

                    if usuario.first_name =='Secretaria':
                        if usuario.secretaria.desabilitado:
                            logout(request)
                            return HttpResponseRedirect('/')
                        else:
                            return HttpResponseRedirect('/secretaria')

                return HttpResponseRedirect('/')
            else:
                # warning
                messages.warning(request, 'Tu cuenta ha sido desactivada.')
                #return HttpResponseRedirect('/')
                return HttpResponse('<h1>ERROR desactivada</h1>')
        else:
            # error
            messages.error(request, 'Nombre de usuario o contraseña errónea.')
            #return HttpResponseRedirect('/')
            return HttpResponse('<h1>ERROR no existe</h1>')
    else:
        return HttpResponseRedirect('/')

def crear_usuario(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = RegisForm(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')

    name = request.POST['username']
    nombres = request.POST['nombres']
    apellidop = request.POST['apellidop']
    apellidom = request.POST['apellidom']
    pass1 = request.POST['password1']
    pass2 = request.POST['password2']
    email1 = request.POST['email1']
    email2 = request.POST['email2']


    if pass1 != pass2:
        return HttpResponse('<h1>Las contraseñas ingresadas no son iguales</h1>')

    if email2 != email1:
        return HttpResponse('<h1>Los Correos ingresados no son iguales</h1>')

    pepito = False
    usuarios = User.objects.all()
    for usuario in usuarios:
        if usuario ==name:
            pepito = True

    if pepito:
        return HttpResponse('<h1>el usuario ya exite</h1>')

    new_user = User(username=name,email=email1,first_name="Paciente")
    new_user.set_password(pass1)
    new_user.save()
    new_paciente = Paciente(user=new_user,nombres=nombres,apellido_p=apellidop,apellido_m=apellidom)
    new_paciente.save()
    user = authenticate(username=name, password=pass1)
    login(request, user)
    return HttpResponseRedirect('/tomahora')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def borrar_hora(request,id_in):
    hora = Agendamiento.objects.get(id=id_in)
    hora.desabilitado = True
    return HttpResponseRedirect('/tomahora')

@login_required
def cambiarpass(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = ModificarP(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')

    usuario =User.objects.get(username=request.user)
    pass1= request.POST['contrasena1']
    if not usuario.check_password(pass1):
        return HttpResponse('<h1>Contraseña actual incorrecta</h1>')
    pass2 =request.POST['contrasena2']
    pass3 = request.POST['contrasena3']

    if pass2 != pass3:
        return HttpResponse('<h1>Las contraseñas ingresadas no son iguales</h1>')

    usuario.set_password(pass3)
    usuario.save()
    return HttpResponseRedirect('/tomahora')

@login_required
def cambiaremail(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = ModificarE(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')

    usuario =User.objects.get(username=request.user)

    email1 =request.POST['correo1']
    email2 = request.POST['correo2']

    if email1 != email2:
        return HttpResponse('<h1>Los correos ingresados no son iguales</h1>')

    usuario.email= email1
    usuario.save()
    return HttpResponseRedirect('/tomahora')

@login_required
def cambiartelefonoc(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = ModificarTc(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')

    usuario =User.objects.get(id=request.user.id)
    paciente = Paciente.objects.get(user = usuario)
    telefonoc1 =request.POST['telefonoc1']
    telefonoc2 = request.POST['telefonoc2']

    if telefonoc1 != telefonoc2:
        return HttpResponse('<h1>Los telefonos ingresados no son iguales</h1>')

    paciente.telefono_c= telefonoc1
    paciente.save()
    return HttpResponseRedirect('/tomahora')

@login_required
def cambiartelefonof(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = ModificarTf(request.POST)

    if not form.is_valid():
        #error = True
        #return render_to_response('tomahora.html',{'error':error},context_instance=RequestContext(request))
        messages.warning(request, 'Tu cuenta ha sido desactivada.')
        return HttpResponse('<h1>Formulario Malo</h1>')

    usuario =User.objects.get(username=request.user)
    paciente = Paciente.objects.get(user = usuario)
    telefonof1 =request.POST['telefonof1']
    telefonof2 = request.POST['telefonof2']

    if telefonof1 != telefonof2:
        return HttpResponse('<h1>Los telefonos ingresados no son iguales</h1>')

    paciente.telefono_f= telefonof1
    paciente.save()
    return HttpResponseRedirect('/tomahora')

@login_required
def agregardentista(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = AgregarDentista(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')

    name = request.POST['username']
    nombres = request.POST['nombres']
    apellidop = request.POST['apellidop']
    apellidom = request.POST['apellidom']
    password = request.POST['password']
    email = request.POST['email']
    telefonoc = request.POST['telefonoc']
    telefonof = request.POST['telefonof']
    run_colegio = request.POST['run_colegio']

    new_user = User(username=name,email=email1,first_name="Dentista")
    new_user.set_password(pass1)
    new_user.save()
    new_dentista = Dentista(user=new_user,nombres=nombres,apellido_p=apellidop,apellido_m=apellidom,telefono_c=telefonoc,telefono_f=telefonof,run_colegio=run_colegio,administrador=False)
    new_dentista.save()
    user = authenticate(username=name, password=pass1)
    login(request, user)
    return HttpResponseRedirect('/')

@login_required
def agregarsecretaria(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = AgregarSecretaria(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')

    name = request.POST['username']
    nombres = request.POST['nombres']
    apellidop = request.POST['apellidop']
    apellidom = request.POST['apellidom']
    password = request.POST['password']
    email = request.POST['email']
    telefonoc = request.POST['telefonoc']
    telefonof = request.POST['telefonof']

    new_user = User(username=name,email=email1,first_name="Dentista")
    new_user.set_password(pass1)
    new_user.save()
    new_secretaria = Secretaria(user=new_user,nombres=nombres,apellido_p=apellidop,apellido_m=apellidom,telefono_c=telefonoc,telefono_f=telefonof,administrador= False)
    new_secretaria.save()
    user = authenticate(username=name, password=pass1)
    login(request, user)
    return HttpResponseRedirect('/')

@login_required
def agregarespecialidad(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = AgregarEspecialidad(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')
    
    nombre = request.POST['nombre']
    cantidad = request.POST['cantidad']

    new_especialidad= Especialidad(nombre=nombre,cantidad_b=cantidad,desabilitado=False)
    new_especialidad.save()
    return HttpResponseRedirect('/')

@login_required
def agregarbox(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = AgregarBox(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')
    
    nombre = request.POST['nombre']

    new_box= Box(nombre=nombre,desabilitado=False)
    new_box.save()
    return HttpResponseRedirect('/')
    
@login_required
def eliminardentista(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = EliminarDentista(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')
    
    dentista = request.POST['username']
    dentista.desabilitado=True
    dentista.save()
    return HttpResponseRedirect('/')

@login_required
def eliminarsecretaria(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = EliminarSecretaria(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')
    
    secretaria = request.POST['username']
    secretaria.desabilitado=True
    secretaria.save()
    return HttpResponseRedirect('/')

@login_required
def eliminarespecialidad(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = EliminarEspecialidad(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')
    
    especialidad = request.POST['identificador']
    especialidad.desabilitado=True
    especialidad.save()
    return HttpResponseRedirect('/')

@login_required
def eliminarbox(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = EliminarBox(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')
    
    box = request.POST['identificador']
    box.desabilitado=True
    box.save()
    return HttpResponseRedirect('/')

@login_required
def asignarespecialidad(request):
    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')
    form = AsignarEspecialidad(request.POST)
    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')
    
    especialidad = request.POST['especialidad']
    username = request.POST['username']

    union = Dentista_especialidad(dentista=username,especialidad=especialidad)
    union.save()
    
    return HttpResponseRedirect('/administrador')

@login_required
def desasignarespecialidad(request):

    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')
    form = DesasignarEspecialidad(request.POST)
    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')
    
    especialidad = request.POST['especialidad']
    username = request.POST['username']

    union = Dentista_especialidad.objects.get(dentista=username,especialidad=especialidad)
    union.delete()
    
    return HttpResponseRedirect('/administrador')

@login_required
def atencion(request):
    return HttpResponseRedirect('/personal')

@login_required
def eliminaroferta(request):
    return HttpResponseRedirect('/personal')

@login_required
def verficha(request):
    return HttpResponseRedirect('/personal')


@login_required
def ingresaroferta(request):
    clicks=request.POST.keys()
    for click in clicks:
        if click == request.POST[click]:
            if click =="11":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
            if click =="21":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="31":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="41":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="51":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="61":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="71":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="81":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="91":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="101":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="111":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="121":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="131":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="141":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="151":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="161":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="2",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="9",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="16",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="23",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="30",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="12":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="22":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="32":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="42":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="52":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="62":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="72":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="82":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="92":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="102":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="112":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="122":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="132":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="142":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="152":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="162":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="3",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="10",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="17",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="24",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="13":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="23":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="33":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="43":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="53":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="63":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="73":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="83":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="93":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="103":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="113":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="123":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="133":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="143":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="153":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="163":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="4",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="11",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="18",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="25",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="14":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="24":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="34":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="44":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="54":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="64":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="74":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="84":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="94":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="104":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="114":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="124":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="134":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="144":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="154":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="164":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="5",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="12",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="19",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="26",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
            if click =="15":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=1)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="25":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=2)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="35":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=3)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="45":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=4)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="55":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=5)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="65":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=6)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="75":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=7)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="85":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=8)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="95":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=9)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="105":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=10)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="115":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=11)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="125":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=12)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="135":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=13)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="145":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=14)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="155":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=15)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
            if click =="165":
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="6",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="13",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="20",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()                
                a=Calendario.objects.get(ano=2013,mes="Septiembre",dia="27",Bloque_horario=16)
                b= Oferta_horaria(disponible=True,dentista=user.dentista,calendario=a)
                b.save()

    return HttpResponseRedirect('/dentista')

def ajaxespecialidad(request):
    a = request.POST['a']
    c = Especialidad.objects.get(nombre=a)
    b= Dentista_especialidad.objects.filter(especialidad=c)
    lista = []
    for u in b:
        lista.append(u.dentista.nombres)
    data = simplejson.dumps(lista)
    return HttpResponse(data, mimetype='application/json')

def ajaxdentista(request):
    a = request.POST['p']
    c = Especialidad.objects.get(nombre=a)
    b= Dentista_especialidad.objects.filter(especialidad=c)
    lista = []
    for u in b:
        lista.append(u.dentista)
        lista.append(",")
    lista.append("pico")
    return HttpResponse(lista)