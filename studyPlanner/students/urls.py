from django.urls import path
from .import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.index, name='index'),
    path('meuPerfil', views.meuPerfil, name='meuPerfil'),
    path('agenda', views.agenda, name='agenda'),
    path('notas', views.notas, name='notas'),
    path('entregas', views.entregas, name='entregas'),
]