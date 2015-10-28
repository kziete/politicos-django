from django.db import models

# Create your models here.

class Politico(models.Model):
	nombre = models.CharField(max_length=128)