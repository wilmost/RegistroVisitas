from django import forms 

from .models import Visitante



# class registrar_visitante(forms.ModelForm):
#     class Meta:
#         model = Visitante
#         fields = [ 
#                 'nombre',
#                 'apellido',
#                 'cedula',
#                 'institucion', 
#                 'posicion',
#                 'email',
#                 'direccion',
#                 'celular',
#                 'motivo', 
#                 'hora' 
#             ] 


            


class registrar_visitante(forms.Form):
    nombre              = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    apellido            = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    cedula              = forms.CharField(max_length = 11, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    institucion         = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    posicion            = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email               = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    direccion           = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    celular             = forms.CharField(max_length = 10, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    motivo              = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    hora                = forms.TimeField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    
#     #forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))