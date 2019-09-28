from django import forms
from .models import Salon

class SalonForm(forms.ModelForm):
	class Meta:
		model = Salon
		fields = ('nombre','cant_alumnos','sede')
		widgets= {
			'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre del Salon'}),
			'cant_alumnos': forms.NumberInput(attrs={'class':'form-control'}),
		}
		labels = {
			'nombre':'Nombre', 'cant_alumnos':'Alumnos','sede':'Sede',
		}