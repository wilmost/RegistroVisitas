"""Registro_visitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view 
from visitante.views import (
     registrar_visitante_view, 
     listado_visistas_view, 
     VisitasListView,
     VisitasDetailView,
     VisitasCreateView,
     VisitasUpdateView,
     VisitasDeleteView

    ) 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view), 
    path('visitante/', registrar_visitante_view), 
    path('reportes/', listado_visistas_view), 
    path('visitante_list/', VisitasListView.as_view(), name = 'visita-lista'),
    path('visita/<int:pk>/', VisitasDetailView.as_view(), name='visita-detail'),
    path('visita/new/', VisitasCreateView.as_view(), name='visita-create'),
    path('visita/<int:pk>/update/', VisitasUpdateView.as_view(), name='visita-update'),
    path('visita/<int:pk>/delete/', VisitasDeleteView.as_view(), name='visita-delete'),
    
]
