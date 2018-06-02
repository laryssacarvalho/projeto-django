from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as viewsDjango

urlpatterns = [
    path('', viewsDjango.login, {'template_name':'core/login.html'}, name='login'),    
    path('home', views.home, name='home'),
    path('user_profile/', views.user_profile),
    path('user_form/', views.create_profile, name='editar'),
    path('logout', viewsDjango.logout, {'next_page' : 'login'}, name='logout')
]
