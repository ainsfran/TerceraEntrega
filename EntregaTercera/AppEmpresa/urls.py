from django.urls import path
from AppEmpresa import views

urlpatterns = [
    path('', views.inicio, name='Home'),
    path('equipos', views.equipos, name='Servicies'),
    path('trabajador', views.trabajador, name='Team'),
    path('projectmanager', views.projectmanager, name='Project Manager'),
    path('proyecto', views.proyecto, name='Projects'),
    #path('equiposFormulario', views.equiposFormulario, name='EquiposFormulario'),
    #path('trabajadorFormulario', views.trabajadorFormulario, name='TrabajadorFormulario'),
    #path('projectmanageFormulario', views.projectmanagerFormulario, name='ProjectmanagerFormulario'),
    #path('proyectoFormulario', views.proyectoFormulario, name='ProyectoFormulario'),
    path('busquedacamada', views.busquedacamada, name='Busquedacamada'),
    path('buscar/', views.buscar),
]
