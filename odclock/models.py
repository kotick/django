# -*- encoding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User

class Paciente(models.Model):
    run = models.CharField('RUN', primary_key=True,max_length=30)
    nombre = models.CharField(max_length=30)
    apellido_p = models.CharField(max_length=30)
    apellido_m = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    telefono_c = models.CharField(max_length=30)
    telefono_f = models.CharField(max_length=30)
    administrador = models.BooleanField()
    ficha = models.TextField()
    prevision = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)

class Dentista(models.Model):
    run_colegio = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido_p = models.CharField(max_length=30)
    apellido_m = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    telefono_c = models.CharField(max_length=30)
    telefono_f = models.CharField(max_length=30)
    administrador = models.BooleanField()
    contrasena = models.CharField(max_length=30)
    run = models.CharField('RUN', primary_key=True, max_length=30)

class Secretaria(models.Model):
    run = models.CharField('RUN', primary_key=True,max_length=30)
    nombre = models.CharField(max_length=30)
    apellido_p = models.CharField(max_length=30)
    apellido_m = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    telefono_c = models.CharField(max_length=30)
    telefono_f = models.CharField(max_length=30)
    administrador = models.BooleanField()
    contrasena = models.CharField(max_length=30)

class Box(models.Model):
    id = models.AutoField('ID', primary_key=True)

class Calendario(models.Model):
    fecha = models.DateField()
    feriado = models.BooleanField()
    id = models.AutoField('ID', primary_key=True)
    Bloque_horario = models.IntegerField(max_length=32)

class Prestacion(models.Model):
    id = models.AutoField('ID', primary_key=True)
    nombre = models.CharField(max_length=30)
    detalles = models.TextField()

class Especialidad(models.Model):
    id = models.AutoField('ID', primary_key=True)
    nombre = models.CharField(max_length=30)
    cantidad_b = models.IntegerField(max_length=32)

class Plan_tratamiento(models.Model):
    id = models.AutoField('ID', primary_key=True)
    especialidad=models.ForeignKey(Especialidad)
    nombre = models.CharField(max_length=30)
    sesiones = models.IntegerField(max_length=30)
    bloques = models.IntegerField(max_length=32)
    detalles = models.TextField()

class Atencion(models.Model):
    id = models.AutoField('ID', primary_key=True)
    tipo = models.IntegerField(max_length=4)
    dentista=models.ForeignKey(Dentista)
    plan_tratamiento= models.ForeignKey(Plan_tratamiento)
    box = models.ForeignKey(Box)
    paciente= models.ForeignKey(Paciente)
    fecha = models.DateTimeField()
    detalles = models.TextField()

class Derivacion(models.Model):
    id = models.AutoField('ID', primary_key=True)
    paciente = models.ForeignKey(Paciente)
    especialidad= models.ForeignKey(Especialidad)
    atencion = models.ForeignKey(Atencion)
    justificacion = models.TextField()

class Oferta_horaria(models.Model):
    id = models.AutoField('ID',primary_key=True)
    disponible = models.BooleanField()
    dentista = models.ForeignKey(Dentista)
    calendario = models.ForeignKey(Calendario)

class Dentista_especialidad(models.Model):
    id = models.AutoField('ID',primary_key=True)
    dentista=models.ForeignKey(Dentista)
    especialidad=models.ForeignKey(Especialidad)


class Especialidad_Box(models.Model):
    id = models.AutoField('ID', primary_key=True)
    especialidad=models.ForeignKey(Especialidad)
    box = models.ForeignKey(Box)

class Plan_prestacion(models.Model):
    id = models.AutoField('ID', primary_key=True)
    plan_tratamiento = models.ForeignKey(Plan_tratamiento)
    prestacion = models.ForeignKey(Prestacion)

class Prestacion_atencion(models.Model):
    id = models.AutoField('ID', primary_key=True)
    prestacion= models.ForeignKey(Prestacion)
    atencion = models.ForeignKey(Atencion)

class Agendamiento(models.Model):
    id = models.AutoField('ID', primary_key=True)
    especialidad = models.ForeignKey(Especialidad)
    dentista = models.ForeignKey(Dentista)
    calendario = models.ForeignKey(Calendario)
    paciente = models.ForeignKey(Paciente)
    secretaria = models.ForeignKey(Secretaria)

class Auditoria(models.Model):
    id = models.AutoField('ID', primary_key=True)
    momento = models.DateTimeField()
    accion = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    tabla = models.CharField(max_length=30)

class Calendario_box(models.Model):
    id = models.AutoField('ID', primary_key=True)
    ocupado = models.BooleanField()
    box=models.ForeignKey(Box)
    calendario=models.ForeignKey(Calendario)
