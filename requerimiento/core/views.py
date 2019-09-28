from django.shortcuts import render, render_to_response
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import SalonForm
from .models import *
# Create your views here.


class HomePageView(TemplateView):
	template_name = 'core/home.html'

def salonListView(request):
	if request.method=='GET':
		try:
			director = Director.objects.get(nombre=request.GET.get('nombre_director'))
			sede = Sede.objects.get(director=director)
			salones = Salon.objects.filter(sede=sede)
		except Exception as e:
			director = False
			salones = False
		if director==False:
			mensaje = 'Escribió mal el nombre del director'
		else:
			mensaje = False
		context = {'salones':salones, 'mensaje':mensaje}
		return render(request,'core/lista.html',context)
	else:
		return render(request,'core/lista.html')

class SalonCreateView(CreateView):
	model = Salon 
	template_name = 'core/salon.html'
	form_class = SalonForm
	success_url = reverse_lazy('home')

