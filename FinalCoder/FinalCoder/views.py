from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from FinalCoder.forms import UserRegisterForm, UserEditForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contrasena = form.cleaned_data['password']
            user = authenticate(username=usuario, password=contrasena)
            if user is not None:
                login (request,user)
                return redirect('Inicio')
            else:
                return render (request, 'login.html',
                    {'form' : form, 'error':'Usuario y Contraseña NO VALIDOS' })        
                
        else:
            return render(request, 'login.html', {'form' : form })
    else:
        form = AuthenticationForm
        return render(request, 'login.html', {'form' : form })
    
def register (request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return HttpResponse (f'Usuario {username} fue creado correctamente')
    else:
        form = UserRegisterForm()
    
    return render (request, 'registro.html', {'form':form})

class UserCreateView(CreateView):
    model=User
    success_url= reverse_lazy('login')
    template_name='registro.html'
    form_class= UserRegisterForm

@login_required
def editar_perfil (request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario.email = data['email']
            usuario.set_password(data['password'])
            # usuario.password1= data['password1']                    
            # usuario.password2= data['password2']
            usuario.save()
            return redirect ('Inicio')
    else:
        form=UserEditForm({'email':usuario.email}) 
    return render (request, 'registro.html',{'form':form})

def mensaje(request):
    return render(request,'mensaje.html')

def AcercaDe(request):
    return render (request,'AcercaDe.html')