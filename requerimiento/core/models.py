from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Director(models.Model):
	nombre = models.CharField(max_length=100, verbose_name="Nombre")
	apellido = models.CharField(max_length=100, verbose_name="Apellido")
	celular = models.IntegerField()
	class Meta:
		verbose_name = 'Director'
		verbose_name_plural = 'Directores'
	def __str__(self):
		return self.nombre

class Sede(models.Model):
	nombre = models.CharField(max_length=100, verbose_name="Nombre de la Sede")
	direccion = models.CharField(max_length=200, verbose_name="Dirección")
	distrito = models.CharField(max_length=100, verbose_name="Distrito")
	director = models.OneToOneField(Director, on_delete=models.CASCADE, verbose_name='Director')
	class Meta:
		verbose_name = 'Sede'
		verbose_name_plural = 'Sedes'
	def __str__(self):
		return self.nombre

class Salon(models.Model):
	nombre = models.CharField(max_length=100, verbose_name="Nombre", unique=True)
	cant_alumnos = models.IntegerField(verbose_name='Cantidad de alumnos', validators=[MinValueValidator(10)])
	sede = models.ForeignKey(Sede,on_delete=models.CASCADE, verbose_name='Sede')	
	class Meta:
		verbose_name='Salon'
		verbose_name_plural='Salones'
	def __str__(self):
		return self.nombre		