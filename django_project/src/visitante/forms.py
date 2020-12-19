from django import forms 

from .models import Visitante



class registrar_visitante(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [ 
                'nombre',
                'apellido',
                'cedula',
                'institucion', 
                'posicion',
                'email',
                'direccion',
                'celular',
                'motivo', 
                'hora' 
            ] 


            


# class registrar_visitante(forms.Form):
#     nombre              = forms.CharField()
#     apellido            = forms.CharField()
#     cedula              = forms.CharField()
#     institucion         = forms.CharField()
#     posicion            = forms.CharField()
#     email               = forms.EmailField()
#     direccion           = forms.CharField()
#     celular             = forms.CharField()
#     motivo              = forms.CharField()
#     hora                = forms.TimeField()
    