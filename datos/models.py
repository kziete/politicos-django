from django.db import models

# Create your models here.

class Politico(models.Model):
	nombre = models.CharField(max_length=128)

class Evento(models.Model):
	politico = models.ForeignKey(Politico)
	nombre = models.CharField(max_length=128)