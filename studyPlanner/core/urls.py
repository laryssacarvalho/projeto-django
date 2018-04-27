from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as viewsDjango

urlpatterns = [    
    # path('', views.index, name='index'), 
    path('editar/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('entrar/', viewsDjango.login, {'template_name':'core/login.html'}, name='login')
    
]
