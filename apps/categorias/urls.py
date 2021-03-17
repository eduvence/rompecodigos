from django.urls import path
from . import views

app_name = 'categorias'
urlpatterns = [
    path('Redactar_N/', views.Redactar_Noticia.as_view(), name='cargar_n'),
    path('Alta_C/', views.Alta_Categorias.as_view(), name='cargar_c'),
    path('Listar_N/', views.Listar_Noticias, name='listar_n'),
  
]