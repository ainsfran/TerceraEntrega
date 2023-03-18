from django.shortcuts import render
from AppEmpresa.models import Equipos, Trabajador, ProjectManager, Proyecto
from django.http import HttpResponse

from AppEmpresa.forms import equiposFormulario, trabajadorFormulario, projectmanagerFormulario, proyectoFormulario

# Create your views here.

def inicio(request):
    
    return render(request, 'inicio.html')
 
def equipos(request):
    
    if request.method == 'POST':
        miFormulario = equiposFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            equipo = Equipos(nombre=informacion['nombre'], camada=informacion['camada'])
            equipo.save()
            return render(request, 'inicio.html')
    
    else:
        miFormulario = equiposFormulario()
 
    return render(request, 'equipos.html', {'miFormulario': miFormulario})

def trabajador(request):
    
    if request.method == 'POST':
        miFormulario = trabajadorFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            trabajador= Trabajador(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            trabajador.save()
            return render(request, 'inicio.html')
    
    else:
        miFormulario = trabajadorFormulario()
 
    return render(request, 'trabajador.html', {'miFormulario': miFormulario})

def projectmanager(request):
    
    if request.method == 'POST':
        miFormulario = projectmanagerFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            projectmanager= ProjectManager(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], 
            profesion=informacion['profesion'])
            projectmanager.save()
            return render(request, 'inicio.html')
    
    else:
        miFormulario = projectmanagerFormulario()
 
    return render(request, 'projectmanager.html', {'miFormulario': miFormulario})

def proyecto(request):
    
    if request.method == 'POST':
        miFormulario = proyectoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            proyecto= Proyecto(nombre=informacion['nombre'], fechaentrega=informacion['fechaentrega'], entregado=informacion['entregado'])
            proyecto.save()
            return render(request, 'inicio.html')
    
    else:
        miFormulario = proyectoFormulario()
 
    return render(request, 'proyecto.html', {'miFormulario': miFormulario})

def busquedacamada(request):

    return render(request, 'busquedacamada.html')

def buscar(request):
    
    if request.GET['camada']:

        camada = request.GET['camada']
        equipos = Equipos.objects.filter(camada__icontains=camada)
       
        return render(request, 'inicio.html', {'equipos':equipos, 'camada':camada} )
    
    else:
        respuesta= 'Esos datos no fueron ingresados' 

    return render(request, 'inicio.html', {'respuesta': respuesta})


