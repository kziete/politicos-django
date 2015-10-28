from django.db import models
from sitio.models import Usuario

# Create your models here.

class Politico(models.Model):
	nombre = models.CharField(max_length=128)

	def __unicode__(self):
		return self.nombre

class Evento(models.Model):
	politico = models.ForeignKey(Politico)
	nombre = models.CharField(max_length=128)
	fuente = models.CharField(max_length=255)
	autor = models.ForeignKey(Usuario)