from contextlib import nullcontext
#from email import message
from importlib.metadata import requires
from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import is_valid_path
from .models import Movie, Artista
from .forms import movieForm, artistaForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate, login
from django.contrib import messages
#from django.contrib.messages import messages
#Operaciones con movies
@login_required
def movies(request):
    busqueda=request.GET.get("buscar")
    cantidad1=request.GET.get("primeros")
    if(cantidad1):
        movies=Movie.OperacionesManager.smaller_than(5)
    else:    
        movies=Movie.OperacionesManager.get_queryset()
    if(cantidad1):
        movies=Movie.OperacionesManager.get_queryset()
    else:    
        movies=Movie.OperacionesManager.smaller_than(5)
    if busqueda:
        movies=Movie.OperacionesManager.busqueda(busqueda)
    return render(request, "Movies/index.html", {'movies': movies})
    

def crear(request):
 formulario = movieForm(request.POST or None, request.FILES or None)
 if formulario.is_valid():
     formulario.save()
     return redirect('Movies')
 return render(request, "Movies/crear.html", {'formulario':formulario})

def editar(request, id):
    print(id)
    movie=Movie.OperacionesManager.get(id=id)
    formulario=movieForm(request.POST or None, request.FILES or None, instance=movie)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('Movies')
    return render(request, "Movies/editar.html", {'formulario': formulario})

def eliminarMovie(request, id):
    movie=Movie.objects.get(id=id)
    movie.delete()
    return redirect('Movies')

#Operaciones con artistas
def artistas(request):
    artista=Artista.OperacionesManager3.all()
    return render(request, "artistas/index.html", {'artistas': artista})

def crearArtista(request):
 formulario = artistaForm(request.POST or None)
 if formulario.is_valid():
     formulario.save()
     return redirect('artistas')
 return render(request, "artistas/crear.html", {'formulario':formulario})

def editarArtista(request, id):
    artista=Artista.objects.get(id=id)
    formulario=artistaForm(request.POST or None, instance=artista)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('artistas')
    return render(request, "artistas/editar.html", {'formulario': formulario})

def eliminarArtista(request, id):
    artista=Artista.objects.get(id=id)
    artista.delete()
    return redirect('artistas')

#Operaciones de usuarios

def buscar(request):
    print(request.GET)
def salir(request):
    logout(request)
    return redirect('/')
def register(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method=='POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"],\
                password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.add_message(request, messages.INFO,"Registro exitoso")
            return redirect(to="/")
        else:
            print("eror")
        data['form']=formulario
    return render(request, 'registration/register.html', data)