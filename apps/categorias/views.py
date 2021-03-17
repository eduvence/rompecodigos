from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Redacción, Categorias
from .forms import Formulario_Alta_Redacción, Formulario_Alta_Categorias


from django.contrib.auth.mixins import LoginRequiredMixin
from django. contrib.auth.decorators import login_required
# Create your views here.

@login_required
def Listar_Noticias(request):
    categorias = Categorias.objects.all()
    ctx = {}
    ctx['p'] = categorias
    return render(request,'base.html', ctx)

class Redactar_Noticia(LoginRequiredMixin, CreateView):
	model = 'Redacción'
	form_class = Formulario_Alta_Redacción
	template_name = 'categorias/nuevanoticia.html'
	success_url = reverse_lazy('base')


class Alta_Categorias(LoginRequiredMixin,CreateView):
	model='Categorias'
	form_class= Formulario_Alta_Categorias
	template_name='categorias/alta_categorias.html'
	success_url= reverse_lazy('base')	