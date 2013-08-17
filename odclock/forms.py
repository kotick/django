# -*- encoding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Rut'}),label= 'RUN')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label= 'Contraseña')

class RegisForm(forms.Form):
	username =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'RUN'}),label= 'RUN')
	nombres =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre'}),label= 'Nombres')
	apellidos =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Apellido'}),label= 'Apellidos')
	email1 =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Correo Electronico'}),label= 'Correo Electronico')
	email2 =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Correo Electronico'}),label= 'Nuevamente el correo electronico')
	password1 =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}),label= 'Contraseña')
	password2 =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}),label= 'Nuevamente la contraseña')


class ModificarP(forms.Form):
	contrasena1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label= 'Contraseña Actual')
	contrasena2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label= 'Nueva Contraseña')
	contrasena3=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label= 'Nueva Contraseña')

class ModificarE(forms.Form):
	correo1=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Correo Electronico'}),label= 'Nuevo Correo Electronico')
	correo2=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Correo Electronico'}),label= 'Nuevo Correo Electronico')

class ModificarTc(forms.Form):
	telefonoc1=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telefono Celular'}),label= 'Nuevo telefono Celular')
	telefonoc2=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telefono Celular'}),label= 'Nuevo telefono Celular')

class ModificarTf(forms.Form):
	telefonof1=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telefono Fijo'}),label= 'Nuevo telefono Fijo')
	telefonof2=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telefono Fijo'}),label= 'Nuevo telefono Fijo')