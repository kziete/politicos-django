from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from django.db.models import Count
from django import forms

from datos.models import *

# Create your views here.
class Home(ListView):
	def get_queryset(self):
		#Corregir esto por una query, que deje fuera los eventos desactivados
		return Politico.objects.all().annotate(total=Count('evento')).order_by('-total')


class DetallePolitico(DetailView):
	model = Politico

class DetalleEvento(DetailView):
	model = Evento

class DenunciaEvento(CreateView):
	fields = ("nombre","fuente")
	model = Evento