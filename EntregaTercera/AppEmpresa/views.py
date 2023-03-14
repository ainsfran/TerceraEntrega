from django.shortcuts import render
from AppEmpresa.models import Equipos
from django.http import HttpResponse
# Create your views here.

def equipo(self):

    equipo = Equipos(nombre = 'BIM', camada = '1')
    equipo.save()
    documentoDeTexto = f'Equipo: {equipo.nombre}    Camada: {equipo.camada}'

    return HttpResponse(documentoDeTexto)
