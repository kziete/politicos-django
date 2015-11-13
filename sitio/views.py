from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,FormView
from django.views.generic.base import ContextMixin
from django.db.models import Count
from django.core.urlresolvers import reverse

import json

from datos.models import *
from forms import *

class Sidebar(ContextMixin):
	def get_context_data(self,**kwargs):
		context = super(Sidebar, self).get_context_data(**kwargs)
		context['politicos'] = Politico.objects.all().annotate(total=Count('evento')).order_by('-total')
		return context



# Create your views here.
class Home(Sidebar,ListView):
	model = Evento


class DetallePolitico(Sidebar,DetailView):
	model = Politico

class DetalleEvento(DetailView):
	model = Evento

class DenunciaEvento(CreateView):
	fields = ("nombre","descripcion","fuente","fecha")
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



class PathReminder(object):
	def get_success_url(self):
		if "path" in self.request.GET:
			return self.request.GET['path']
		else:
			return "/"

class LoginView(PathReminder,FormView):
	template_name = 'login.html'
	form_class = LoginForm

	def form_valid(self, form):
		usuario = form.logear()

		if usuario is not None:
			self.request.session['usuario'] = usuario.id
			return super(LoginView, self).form_valid(form)
		else:
			return super(LoginView, self).form_invalid(form)

	


class RegistroView(PathReminder,FormView):
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
