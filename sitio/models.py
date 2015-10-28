from django.db import models

# Create your models here.
class Usuario(models.Model):
	email = models.CharField(max_length=255)

	def __unicode__(self):
		return self.email