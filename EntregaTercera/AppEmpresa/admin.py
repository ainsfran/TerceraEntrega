from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Equipos)

admin.site.register(Trabajador)

admin.site.register(ProjectManager)

admin.site.register(Proyecto)