from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home_view(request,*args, **kwargs):
    return render(request, 'home.html', {})


# def registrar_visitante(request,*args, **kwargs):  
#     return render(request, 'registro.html', {})
