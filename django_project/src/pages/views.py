from django.shortcuts import render
from visitante.models import Visitante
import datetime
from django.utils import timezone
from django.http import HttpResponse
from visitante.forms import registrar_visitante

# Create your views here.

# def home_view(request,*args, **kwargs):
#     return render(request, 'home.html', {})


# def registrar_visitante(request,*args, **kwargs):  
#     return render(request, 'registro.html', {})
def home_view(request, *args, **kwargs):
    queryset = Visitante.objects.filter(fecha = datetime.date.today()) 
    print (queryset)
   
    context= {
        'object_list' : queryset,
       
    }
    return render (request, 'home.html',context)

def registrar_entrara_form(request, pk): 
    
    #if form.is_valid(): 
    
    context = {}

    return render (request, 'home.html', context )