from .views import HomePageView, salonListView, SalonCreateView
from django.urls import path

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('salones/', salonListView, name='lista'),
	path('Crear-salon/', SalonCreateView.as_view(), name='crear'),
]