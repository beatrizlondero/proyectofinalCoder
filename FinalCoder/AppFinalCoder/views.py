# from datetime import datetime
# from re import template
from asyncio.windows_events import NULL
from datetime import date
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
from AppFinalCoder.forms import productosForm, AvatarFormulario, ComentarioFormulario 
from AppFinalCoder.models import Cliente, Avatar
from AppFinalCoder.models import Productos
from AppFinalCoder.models import Comentarios

def llamar_avatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url= avatares.last().imagen.url
    else:
        avatar_url = "ninguna"
    return avatar_url

# @login_required
def inicio (request):
    # avatares = Avatar.objects.filter(user=request.user.id)
    # if avatares:
    #     avatar_url= avatares.last().imagen.url
    # else:
    #     avatar_url = "ninguna"
    avatar_url = llamar_avatar(request)
        
    return render(request,'AcercaDe.html',{'avatar_url':avatar_url})
    

def proveedores(request):
    avatar_url = llamar_avatar(request)
    return render(request, 'proveedor_inicio.html',{'avatar_url':avatar_url})

def clientes(request):
    avatar_url = llamar_avatar(request)
    return render(request, 'cliente_inicio.html',{'avatar_url':avatar_url})

def productos(request):
    avatar_url = llamar_avatar(request)
    return render (request, 'producto_inicio.html',{'avatar_url':avatar_url})

def comentarios(request):
    avatar_url = llamar_avatar(request)
    return render (request, 'comentario_inicio.html',{'avatar_url':avatar_url})
  
class proveedorListView(ListView):
    model = Proveedor
    template_name=('listado.html')  
    
class clienteListView(ListView):
    model = Cliente
    template_name='listadocliente.html'  

class productoListView(ListView):
    model = Productos
    template_name='listadoproducto.html'      

class proveedoresModif(LoginRequiredMixin,ListView):
    model = Proveedor
    template_name='proveedor_edit.html' 
     
class clientesModif(LoginRequiredMixin,ListView):
    model = Cliente
    template_name='clienteedit.html'   
    
class productosModif(LoginRequiredMixin,ListView):
    model = Productos
    template_name='producto_edit.html'  
    
class comentariosModif(LoginRequiredMixin,ListView):
    model = Comentarios
    template_name='comentario_editar.html'      

@login_required
def agregar_comentario(request):
    if request.method == 'POST':
        formulario = ComentarioFormulario(request.POST)
        if formulario.is_valid():
            # formulario = formulario.cleaned_data()
            comentario = Comentarios (user=request.user,
                                      comentario = formulario.cleaned_data['comentario'])
            comentario.save()
            return redirect ('comentarios')
    else :
        formulario = ComentarioFormulario()
    avatar_url = llamar_avatar(request)    
    return render (request, 'comentario_agregar.html', {'form':formulario,'avatar_url':avatar_url})  


class comentarioCreateView(LoginRequiredMixin, CreateView): 
    model = Comentarios
    success_url = reverse_lazy('comentarios')
    fecha = date.today
    
    fields=['user','comentario']
    template_name= 'comentario_agregar.html'  

@login_required    
def agregar_avatar(request):
    if request.method == 'POST':
        formulario = AvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            avatar = Avatar (user=request.user, imagen = formulario.cleaned_data['imagen'])
            avatar.save()
            return redirect ('inicio')
    else :
        formulario = AvatarFormulario()
    avatar_url = llamar_avatar(request)    
    return render (request, 'agregar_avatar.html', {'form':formulario,'avatar_url':avatar_url})        
    
    
class proveedorDeleteView(LoginRequiredMixin,DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedoresList')
    template_name= 'proveedor_form_borrar.html' 
    
class clienteDeleteView(LoginRequiredMixin,DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientesList')
    template_name= 'clienteform_borrar.html' 
    
class productoDeleteView(LoginRequiredMixin,DeleteView):
    model = Productos
    success_url = reverse_lazy('productosList')
    template_name= 'productoform_borrar.html'     

class comentarioDeleteView(LoginRequiredMixin,DeleteView):
    model = Comentarios
    success_url = reverse_lazy('comentarios')
    template_name= 'comentario_delete.html'         
    
    
class proveedoresBorrar(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name='proveedorborrar.html' 

class comentariosBorrar(LoginRequiredMixin, ListView):
    model = Comentarios
    template_name='comentario_borrar.html'     

   
class clientesBorrar(LoginRequiredMixin, ListView):
    model = Cliente
    template_name='clienteborrar.html' 
    
class productosBorrar(LoginRequiredMixin, ListView):
    model = Productos
    template_name='producto_borrar.html'     
    
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
    

class productoCreateView(LoginRequiredMixin, CreateView): 
    model = Productos
    success_url = reverse_lazy('productosList')
    fields=['nombre','descripcion','cantidad'
            ,'precio', 'imagen']
    template_name= 'productoform.html'     
  

class proveedorUpdateView(LoginRequiredMixin,UpdateView):    
    model = Proveedor
    success_url = reverse_lazy('proveedoresList')
    fields=['nombre','domicilio','email' ]
    template_name= 'proveedor_form.html'  
    
class clienteUpdateView(LoginRequiredMixin,UpdateView):    
    model = Cliente
    success_url = reverse_lazy('clientesList')
    fields=['nombre','apellido','nacimiento','email' ]
    template_name= 'clienteform.html'  
    
class productoUpdateView(LoginRequiredMixin,UpdateView):    
    model = Productos
    success_url = reverse_lazy('productosList')
    fields=['nombre','descripcion','cantidad','precio']
    template_name= 'productoForm.html'  
    
class comentarioUpdateView(LoginRequiredMixin,UpdateView):    
    model = Comentarios
    success_url = reverse_lazy('comentarios')
    fields=['comentario']
    template_name= 'comentario_agregar.html'          
    
# class comentarioCreateView(LoginRequiredMixin, CreateView): 
#     model = Comentarios
#     success_url = reverse_lazy('comentarios')
#     fecha = date.today
    
#     fields=['user','comentario']
#     template_name= 'comentario_agregar.html'      