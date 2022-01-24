from re import template
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from AppFinalCoder.models import Proveedor
from AppFinalCoder.forms import *
# from .models import Curso, Profesor
# from AppCoder.forms import CursoForm , ProfesorForm
def inicio (request):
    return render(request,'inicio.html')
    # return HttpResponse("Incio")

def proveedores(request):
    return render(request, 'inicio.html')

# def proveedoresList(request):
#     return render(request, 'listado.html', {'proveedor' :Proveedor.objects.all()})

def proveedoresAdd(request):
    if request.method=='POST':
        formulario = proveedorForm (request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Proveedor.objects.create(nombre=data['nombre'], domicilio=data['domicilio'],email=data['email'])
            return redirect('proveedoresList')
    else:
        formulario = proveedorForm()
    return render(request, 'proveedor.html',{'formulario': formulario})      

def proveedoresDel(request,proveedorNombre):
      proveedor = Proveedor.objects.get(nombre=proveedorNombre)
      proveedor.delete()
      return redirect('proveedores') 
  
class proveedorListView(ListView):
    model = Proveedor
    template_name='listado.html'  
    # context_objet_name= 'proveedores'
    
    