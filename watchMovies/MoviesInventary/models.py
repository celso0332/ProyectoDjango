
from django.db import models
from .manager import operaciones1, operaciones3
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Movie(models.Model):
  id=models.AutoField(primary_key=True)
  titulo=models.CharField(max_length=100, verbose_name="Titulo")
  portada=models.ImageField(upload_to='images/',null=True, verbose_name="Portada")
  sinopsis=models.TextField(null=True, verbose_name="Sinopsis")
  OperacionesManager=operaciones1()
  
  def __str__(self):
    fila="Titulo: "+self.titulo+"--Sinopsis: "+self.sinopsis
    return fila
  
  def delete(self, using=None, keep_parents=False):
    self.portada.storage.delete(self.portada.name)
    super().delete()
  
class Artista(models.Model):
  id=models.AutoField(primary_key=True)
  nombre=models.CharField(max_length=50, verbose_name="Nombre")
  edad=models.IntegerField(null=True, verbose_name="Edad")
  recorrido=models.TextField(null=True, verbose_name="Historia")
  OperacionesManager3=operaciones3()
  def __str__(self):
    fila="--Nombre: "+self.nombre
    return fila
