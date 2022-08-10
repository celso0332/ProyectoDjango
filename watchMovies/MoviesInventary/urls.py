from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
#from .views import register
urlpatterns = [
    #Principal
    path('', views.movies, name="Movies"),
    #Operaciones de Movies
    path('Movies', views.movies, name="Movies"),
    path('Movies/crear',views.crear, name='crear'),
    path('Movies/editar/<int:id>', views.editar, name='editar'),
    path('eliminarMovie/<int:id>', views.eliminarMovie, name='eliminarMovie'),
     #Operaciones de Artistas
    path('artistas',views.artistas, name='artistas'),
    path('artistas/crear',views.crearArtista, name='crearArtista'),
    path('eliminarArtista/<int:id>', views.eliminarArtista, name='eliminarArtista'),
    path('artistas/editarArtista/<int:id>', views.editarArtista, name='editarArtista'),
    path('register/', views.register, name='register'),
    #Operaciones de usuarios

    path('salir', views.salir, name='salir'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
