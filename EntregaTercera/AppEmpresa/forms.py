from django import forms

class equiposFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()


class trabajadorFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class projectmanagerFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class proyectoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    fechaentrega = forms.DateField()
    entregado = forms.BooleanField()
