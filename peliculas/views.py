from django.shortcuts import render

from django.http import HttpResponse

from .models import Pelicula,Genero,Director

def index(request):
    
    pelis = Pelicula.objects.all().count()
    directores = Director.objects.all().count()
    generos = Genero.objects.all().count()
    
    return render(
        request,
        "index.html",
        context = {
            'cpeliculas': pelis,
            'cdirectores': directores,
            'cgeneros': generos
        }
        
    )


def directores(request):
    directores = Director.objects.all()

    return render(
        request,
        "directores.html",
        context = {
            'directores': directores,
        }
        
    )

def verdirector(request, idd=None):

    director = Director.objects.get(pk=idd)

    peliculas = director.pelicula_set.all()

    
    return render(
        request,
        "director.html",
        context = {
            'director':director,
            'peliculas': peliculas
        }
        
    )


def verpelicula(request, idd=None):
    
    pelicula = Pelicula.objects.get(pk=idd)
    #backurl = request.META.get('HTTP_REFERER')

    return render(
        request,
        "pelicula.html",
        context = {
            'pelicula': pelicula,
            #'backurl' : backurl
        }
        
    )