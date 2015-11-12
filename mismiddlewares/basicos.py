# -*- encoding: utf-8 -*-
from django.shortcuts import redirect
from sitio.models import Usuario

class Autenticacion:
	def process_view(self,request, view_func, view_args, view_kwargs):

		request.usuario = None

		if "usuario" in request.session:
			request.usuario = request.session['usuario']

		if request.path.endswith("/denuncia") and not request.usuario:
			return redirect("/login?path={0}".format(request.path))
		else:
			return view_func(request,*view_args,**view_kwargs)


	def process_template_response(self,request,response):
		if request.usuario:
			response.context_data['usuario'] = Usuario.objects.get(id=request.usuario)

		if "path" in request.GET:
			response.context_data['referer_path'] = "?path={0}".format(request.GET['path'])

		return response