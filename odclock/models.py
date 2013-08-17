# -*- encoding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User

class Paciente(models.Model):
    user = models.OneToOneField(User,primary_key=True)
    nombre = models.CharField(max_length=30)
    telefono_c = models.CharField(max_length=30)
    telefono_f = models.CharField(max_length=30)
    administrador = models.BooleanField()
    ficha = models.TextField()
    prevision = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)
    desabilitado = models.BooleanField()

class Dentista(models.Model):
    user = models.OneToOneField(User,primary_key=True)
    run_colegio = models.CharField(max_length=30)
    telefono_c = models.CharField(max_length=30)
    telefono_f = models.CharField(max_length=30)
    administrador = models.BooleanField()
    contrasena = models.CharField(max_length=30)
    desabilitado = models.BooleanField()

class Secretaria(models.Model):
    user = models.OneToOneField(User,primary_key=True)
    telefono_c = models.CharField(max_length=30)
    telefono_f = models.CharField(max_length=30)
    administrador = models.BooleanField()
    contrasena = models.CharField(max_length=30)
    desabilitado = models.BooleanField()

class Box(models.Model):
    desabilitado = models.BooleanField()

class Calendario(models.Model):
    fecha = models.DateField()
    feriado = models.BooleanField()
    Bloque_horario = models.IntegerField(max_length=32)

class Prestacion(models.Model):
    nombre = models.CharField(max_length=30)
    detalles = models.TextField()
    desabilitado = models.BooleanField()

class Especialidad(models.Model):
    nombre = models.CharField(max_length=30)
    cantidad_b = models.IntegerField(max_length=32)
    desabilitado = models.BooleanField()

class Plan_tratamiento(models.Model):
    especialidad=models.ForeignKey(Especialidad)
    nombre = models.CharField(max_length=30)
    sesiones = models.IntegerField(max_length=30)
    bloques = models.IntegerField(max_length=32)
    detalles = models.TextField()
    desabilitado = models.BooleanField()

class Atencion(models.Model):
    tipo = models.IntegerField(max_length=4)
    dentista=models.ForeignKey(Dentista)
    plan_tratamiento= models.ForeignKey(Plan_tratamiento)
    box = models.ForeignKey(Box)
    paciente= models.ForeignKey(Paciente)
    fecha = models.DateTimeField()
    detalles = models.TextField()
    desabilitado = models.BooleanField()

class Derivacion(models.Model):
    paciente = models.ForeignKey(Paciente)
    especialidad= models.ForeignKey(Especialidad)
    atencion = models.ForeignKey(Atencion)
    justificacion = models.TextField()
    desabilitado = models.BooleanField()

class Oferta_horaria(models.Model):
    disponible = models.BooleanField()
    dentista = models.ForeignKey(Dentista)
    calendario = models.ForeignKey(Calendario)
    desabilitado = models.BooleanField()

class Dentista_especialidad(models.Model):
    dentista=models.ForeignKey(Dentista)
    especialidad=models.ForeignKey(Especialidad)


class Especialidad_Box(models.Model):
    especialidad=models.ForeignKey(Especialidad)
    box = models.ForeignKey(Box)

class Plan_prestacion(models.Model):
    plan_tratamiento = models.ForeignKey(Plan_tratamiento)
    prestacion = models.ForeignKey(Prestacion)

class Prestacion_atencion(models.Model):
    prestacion= models.ForeignKey(Prestacion)
    atencion = models.ForeignKey(Atencion)

class Agendamiento(models.Model):
    especialidad = models.ForeignKey(Especialidad)
    dentista = models.ForeignKey(Dentista)
    calendario = models.ForeignKey(Calendario)
    paciente = models.ForeignKey(Paciente)
    secretaria = models.ForeignKey(Secretaria)
    desabilitado = models.BooleanField()

class Auditoria(models.Model):
    momento = models.DateTimeField()
    accion = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    tabla = models.CharField(max_length=30)

class Calendario_box(models.Model):
    ocupado = models.BooleanField()
    box=models.ForeignKey(Box)
    calendario=models.ForeignKey(Calendario)