from django.shortcuts import render
from .models import Visitante
from .forms import registrar_visitante
# Create your views here.

def registrar_visitante_view(request): 
    form = registrar_visitante(request.POST or None)
    if form.is_valid():
        form.save() 
        form = registrar_visitante()
    context = {
        'form': form
    }
    return render(request, 'visitantes/visitante.html', context) 


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
                'Hora de entrada' ]
   
    context_ = {
        'object_list': queryset, 
        'header': header
    } 
    return render(request,'visitantes/visitas.html', context_)