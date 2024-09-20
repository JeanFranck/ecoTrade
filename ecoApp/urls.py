from django.urls import path, include
from . import views

app_name = 'ecoApp'

urlpatterns = [
    path('', views.inicio , name = 'inicio'),
    path('perfil', views.perfil, name = 'perfil'),
    path('crearNivel', views.crearNivel, name='crearNivel'),
    path('crearGrado', views.crearGrado, name='crearGrado'),
    path('crearSeccion', views.crearSeccion, name='crearSeccion')
]
