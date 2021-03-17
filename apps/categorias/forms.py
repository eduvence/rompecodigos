from django import forms
from django.db.models.base import Model
from .models import Categorias, Redacción

class Formulario_Alta_Redacción(forms.ModelForm):
    class Meta:
        model = Redacción
        fields = '__all__'

class Formulario_Alta_Categorias(forms.ModelForm):

	class Meta:
		model=Categorias
		fields= '__all__'