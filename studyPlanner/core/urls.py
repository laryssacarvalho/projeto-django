from django.urls import path
from django.urls import include
from .import views


urlpatterns = [    
    path('', views.index, name='index'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('home/',views.home_view,name='home')

]   