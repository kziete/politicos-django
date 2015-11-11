from django import forms
from models import Usuario

class LoginForm(forms.Form):
	email = forms.CharField()
	password = forms.CharField()

	def logear(self):
		cleaned_data = super(LoginForm, self).clean()

		try:
			return Usuario.objects.get(email=cleaned_data['email'],password=cleaned_data['password'])
		except Exception, e:
			self.add_error(None,"Usuario no encontrado")
			return None
