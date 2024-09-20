from django.db import models

# Create your models here.

class nivel (models.Model):
    nombreNivel = models.CharField(max_length=48, null=True, blank=True)

class grado (models.Model):
    nombreGrado = models.CharField(max_length=48, null=True, blank=True)
    nivelRelacionado = models.ForeignKey(nivel, null=True, blank=True, on_delete=models.SET_NULL)

class seccion (models.Model):
    nombreSeccion = models.CharField(max_length=48, null=True, blank=True)
    nivelRelacionado = models.ForeignKey(nivel, null=True, blank=True, on_delete=models.SET_NULL)
    gradoRelacionado = models.ForeignKey(grado, null=True, blank=True, on_delete=models.SET_NULL)