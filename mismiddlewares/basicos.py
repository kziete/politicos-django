# -*- encoding: utf-8 -*-
from django.shortcuts import redirect

class Autenticacion:
    def process_view(self,request, view_func, view_args, view_kwargs):

        request.usuario = None

        if "usuario" in request.session:
            request.usuario = request.session['usuario']

        #Aca pueden ser las reglas que quieran,
        #en mi caso estoy aplicando la restricción
        #a cualquier url que empiece con "usuario"
        if request.get_full_path().endswith("/denuncia") and not request.usuario:
            return redirect("/login?path={0}/lol".format(request.get_full_path()))
        else:
            return view_func(request,*view_args,**view_kwargs)
