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
from AppFinalCoder.models import Cliente, Avatar

@login_required
def inicio (request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url= avatares.last().imagen.url
    else:
        avatar_url =''
        
    return render(request,'AcercaDe.html',{'avatar_url':avatar_url})
    # return HttpResponse("Incio")
    # avatares = Avatar.objects.filter(user=request.user.id)
    # return render (request, 'inicio.html',{'url':avatares[0].imagen.url})
    

def proveedores(request):
    return render(request, 'proveedor_inicio.html')

def clientes(request):
    return render(request, 'cliente_inicio.html')
  
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

@login_required    
def agregar_avatar(request):
    if request == 'POST':
        formulario = AvatarFomrulario(request.POST, request.FILES)
        if formulario.is_valid():
            avatar = Avatar (user=request.user, imagen = formulario.cleaned_data['imagen'])
            avatar.save
            return redirect ('inicio')
    else :
        formulario = AvatarFomrulario()
    return render (request, 'agregar_avatar.html', {'form':formulario})        
    
    
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
    template_name='proveedorborrar.html' 
    
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
    template_name= 'clienteform.html'  