from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Movie, Artista
from django.contrib.auth.forms import UserCreationForm
class movieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'
        
        
        
class artistaForm(forms.ModelForm):
    class Meta:
       model=Artista
       fields='__all__'




class entrarForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

class CustomUserCreationForm(UserCreationForm):
    pass
