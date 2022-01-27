from re import template
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from AppFinalCoder.models import Proveedor
from AppFinalCoder.forms import *
from AppFinalCoder.models import Cliente

@login_required
def inicio (request):
    return render(request,'inicio.html')
    # return HttpResponse("Incio")

def proveedores(request):
    return render(request, 'inicio.html')

def clientes(request):
    return render(request, 'inicio.html')
  
class proveedorListView(ListView):
    model = Proveedor
    template_name='listado.html'  
    
class clienteListView(ListView):
    model = Cliente
    template_name='listadocliente.html'  

class proveedoresModif(LoginRequiredMixin,ListView):
    model = Proveedor
    template_name='proveedor_edit.html' 
     
class clientesModif(LoginRequiredMixin,ListView):
    model = Cliente
    template_name='clienteedit.html'     
    
    
class proveedorDeleteView(DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedoresList')
    template_name= 'proveedor_form_borrar.html' 
    
class clienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientesList')
    template_name= 'clienteform_borrar.html' 
    
class proveedoresBorrar(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name='proveedor_borrar.html' 
    
class clientesBorrar(LoginRequiredMixin, ListView):
    model = Cliente
    template_name='clienteborrar.html' 
    
class proveedorCreateView(LoginRequiredMixin, CreateView): 
    model = Proveedor
    success_url = reverse_lazy('proveedoresList')
    fields=['nombre','domicilio','email' ]
    template_name= 'proveedor_form.html'  
    
class clienteCreateView(LoginRequiredMixin, CreateView): 
    model = Cliente
    success_url = reverse_lazy('clientesList')
    fields=['nombre','apellido','nacimiento'
            ,'email']
    template_name= 'clienteform.html'       

class proveedorUpdateView(UpdateView):    
    model = Proveedor
    success_url = reverse_lazy('proveedoresList')
    fields=['nombre','domicilio','email' ]
    template_name= 'proveedor_form.html'  
    
class clienteUpdateView(UpdateView):    
    model = Cliente
    success_url = reverse_lazy('clientesList')
    fields=['nombre','apellido','nacimiento','email' ]
    template_name= 'cliente_form.html'  