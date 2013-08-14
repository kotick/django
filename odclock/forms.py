# -*- encoding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Rut'}),label= 'RUN')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label= 'Contraseña')

class RegisForm(forms.Form):
	username =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'RUN'}),label= 'RUN')
	nombres =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Rut'}),label= 'Nombres')
	apellidos =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Rut'}),label= 'Apellidos')
	email =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'email'}),label= 'Correo Electronico')
	email =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Correo Electronico'}),label= 'Nuevamente el correo electronico')
	password1 =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label= 'Contraseña')
	password2 =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label= 'Nuevamente la contraseña')