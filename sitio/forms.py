# -*- encoding: utf-8 -*-
from django import forms
from models import Usuario

class LoginForm(forms.Form):
	email = forms.CharField()
	password = forms.CharField()

	def logear(self):
		cleaned_data = super(LoginForm, self).clean()

		try:
			return Usuario.objects.get(email=cleaned_data['email'],password=cleaned_data['password'])
		except Usuario.DoesNotExist, e:
			self.add_error(None,"Usuario no encontrado")
			return None

class RegistrarForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField()
	re_password = forms.CharField()

	def registrar(self):
		cleaned_data = super(RegistrarForm,self).clean()

		if cleaned_data['password'] != cleaned_data['re_password']:
			self.add_error(None,"Las contraseñas no coinciden")
			return None

		try:
			Usuario.objects.get(email=cleaned_data['email'])
			self.add_error(None,"Usuario repetido")
			return None
		except Usuario.DoesNotExist, e:
			usuario = Usuario()
			usuario.email = cleaned_data['email']
			usuario.password = cleaned_data['password']

			usuario.save()

			return usuario
