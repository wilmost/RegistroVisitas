from django.shortcuts import render
from .models import Visitante, Instituciones
from .forms import registrar_visitante
import datetime 
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

# Create your views here.

class VisitasListView(ListView): 
    model = Visitante
    template_name = 'visitantes/visitante_list.html'
    #ordering = ['fecha']

class VisitasDetailView(DetailView): 
    model = Visitante 
    template_name = 'visitantes/visitante_detail.html' 




class VisitasCreateView(CreateView): 
    model = Visitante
    field = fields = [ 
                'nombre',
                'apellido',
                'cedula',
                'institucion', 
                'posicion',
                'email',
                'direccion',
                'celular',
                'motivo', 
                'hora',
                'fecha'
    ] 
    template_name = 'visitantes/visitante_form.html'  

class VisitasUpdateView(UpdateView): 
    model = Visitante 
    field = fields = [ 
                'nombre',
                'apellido',
                'cedula',
                'institucion', 
                'posicion',
                'email',
                'direccion',
                'celular',
                'motivo', 
                'hora',
                'fecha'
    
    ]   
    template_name = 'visitantes/visitante_form.html' 

class VisitasDeleteView(DeleteView): 
    model = Visitante 
    template_name = 'visitantes/visitante_confirm_delete.html'   
    success_url = '/visitante_list'




def registrar_visitante_view(request): 
    form = registrar_visitante(request.POST or None)
    if form.is_valid():
        form.save() 
        form = registrar_visitante()
    context = {
        'form': form
    }
    return render(request, 'visitantes/visitante.html', context) 


def manejo_visitas_view (request): 
    context = {
        'visitas': Visitante.objects.all()
     }
    return render(request, 'visitantes/control_visitas.html', context)
 


def listado_visistas_view(request, *args, **kwargs):  
    queryset = Visitante.objects.all() 
    header = [
                'Nombre',
                'Apellido',
                'Cedula',
                'Institucion', 
                'Posicion',
                'Email',
                'Direccion',
                'Celular',
                'Motivo de la visita', 
                'Hora de entrada',
                'Hora de Salida',
                'Fecha' ]
   
    context_ = {
        'object_list': queryset, 
        'header': header
    } 
    return render(request,'visitantes/reportes.html', context_)


 