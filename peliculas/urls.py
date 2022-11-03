from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('directores', views.directores, name='directores'),
    url(r'^directores/(?P<idd>\d+)$',views.verdirector,name='verdirector'),
    url(r'^pelicula/(?P<idd>\d+)$',views.verpelicula,name='verpelicula'),
]

