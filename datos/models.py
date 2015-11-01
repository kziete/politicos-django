from django.db import models
from sitio.models import Usuario
from django.template.defaultfilters import slugify


# Create your models here.

class Politico(models.Model):
	nombre = models.CharField(max_length=128)
	slug = models.SlugField(('slug'), max_length=60, blank=True)

	def eventos(self):
		return self.evento_set.all().order_by("-fecha")

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Politico, self).save(*args, **kwargs)

class Evento(models.Model):
	politico = models.ForeignKey(Politico)
	nombre = models.CharField(max_length=128)
	fuente = models.CharField(max_length=255)
	autor = models.ForeignKey(Usuario)


	fecha = models.DateTimeField()

	activo = models.BooleanField(default=True)
	creacion = models.DateTimeField(auto_now_add=True)

	slug = models.SlugField(('slug'), max_length=128, blank=True)

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Evento, self).save(*args, **kwargs)

class Campana(models.Model):
	nombre = models.CharField(max_length=128)


class PoliticoCampana(models.Model):
	campana = models.ForeignKey(Campana)
	politico = models.ForeignKey(Politico)