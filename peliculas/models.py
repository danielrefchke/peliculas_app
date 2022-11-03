from django.db import models

# Create your models here.

class Director(models.Model): 
    nombre = models.CharField(max_length = 200,help_text= "Nombre del director")
    
    def __str__(self):
        return self.nombre 

class Genero(models.Model): 
    nombre = models.CharField(max_length = 100,help_text= "Nombre del genero")
    
    def __str__(self):
        return self.nombre 

class Pelicula(models.Model): 
    titulo = models.CharField(max_length = 200,help_text= "Titulo de la pelicula")
    fecha = models.DateField(help_text= "Fecha de estreno de la pelicula",null = True)
    director = models.ForeignKey('Director',on_delete=models.CASCADE)
    resumen = models.TextField(help_text= "Titulo de la pelicula",null = True)
    genero = models.ManyToManyField(Genero)
    
    def __str__(self):
        return self.titulo 
