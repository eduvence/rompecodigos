from django.db import models
from django.db.models.fields import CharField



# Create your models here.
#categorias_status=[
#    (1, 'Internacionales'),
#    (2, 'Nacionales'),
#    (3, 'Policiales'),
#    (4, 'Deportes'),
#]

class Categorias(models.Model):
	nombre=models.CharField(max_length= 50)


	def __str__(self):
		return self.nombre

class Redacción(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField() 
    fecha = models.DateField(auto_now_add=False, auto_now=False, blank=True)
  #  categoria = models.IntegerField(
  #      null=False, blank=False,
  #      choices=categorias_status
  #  )
#    imagen = models.ImageField()

    def __str__(self):
        return (self.nombre)