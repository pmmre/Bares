from django import forms
from django.contrib.auth.models import User
from rango.models import Bar,Tapa,UserProfile


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)


class TapaForm(forms.ModelForm):
	class Meta:
		model = Tapa
		fields = ('nombre_tapa', 'descripcion', 'imagen',)

"""
class BarForm(forms.ModelForm):
    nombre_bar = models.CharField(max_length=128, help_text="El maximo de caractes a introducir es de 128")
    descripcion_bar = models.CharField(max_length=128,help_text="El maximo de caractes a introducir es de 128")


class TapaForm(forms.ModelForm):	    
	nombre_tapa = models.CharField(max_length=50, help_text="El maximo de caractes a introducir es de 128")
    descripcion = models.CharField(max_length=128,help_text="El maximo de caractes a introducir es de 128")
"""


