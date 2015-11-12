from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,FormView
from django.db.models import Count
from django.core.urlresolvers import reverse

import json

from datos.models import *
from forms import *

class Contenedor(object):
	pass

# Create your views here.
class Home(ListView,Contenedor):
	def get_queryset(self):
		#Corregir esto por una query, que deje fuera los eventos desactivados
		return Politico.objects.all().annotate(total=Count('evento')).order_by('-total')


class DetallePolitico(DetailView):
	model = Politico

class DetalleEvento(DetailView):
	model = Evento

class DenunciaEvento(CreateView):
	fields = ("nombre","fuente","fecha")
	model = Evento

	def form_valid(self,form):
		data = form.save(commit=False)
		data.autor = Usuario.objects.get(id=self.request.usuario)
		data.politico = Politico.objects.get(slug=self.kwargs["politico"])

		data.save()

		return HttpResponseRedirect(reverse('detalle-politico', kwargs={"slug" :data.politico.slug}))
    	
def logout(request):
	del request.session['usuario']
	return redirect("/")

class LoginView(FormView):
	template_name = 'login.html'
	form_class = LoginForm

	def form_valid(self, form):
		usuario = form.logear()

		if usuario is not None:
			self.request.session['usuario'] = usuario.id
			return super(LoginView, self).form_valid(form)
		else:
			return super(LoginView, self).form_invalid(form)

	def get_success_url(self):
		if "path" in self.request.GET:
			return self.request.GET['path']
		else:
			return "/"


class RegistroView(FormView):
	template_name = 'registro.html'
	form_class = RegistrarForm
	success_url = "/"

	def form_valid(self,form):
		usuario = form.registrar()

		if usuario is not None:
			self.request.session['usuario'] = usuario.id
			return super(RegistroView, self).form_valid(form)
		else:
			return super(RegistroView, self).form_invalid(form)