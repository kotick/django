# -*- encoding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'span2','type':'password','placeholder':'Email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'span2','type':'password','placeholder':'Password'}))

class RegisForm(forms.Form):
	username =forms.CharField()
	password1 =forms.CharField(widget=forms.PasswordInput())
	password2 =forms.CharField(widget=forms.PasswordInput())