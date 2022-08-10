from django.db import models
class operaciones1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()
    
    def get_querysetid(self,id):
        return super().get_queryset().filter(id=id)
    def smaller_than(self,id):
        return self.filter(id__lt=id)
 
    def busqueda(self,name):
        resultado=self.get_queryset().filter(titulo=name)
        print(resultado)
        return resultado
    
class operaciones3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()
    def get_queryset2(self, name):
        return super().get_queryset().filter(nombre=name)
    
    