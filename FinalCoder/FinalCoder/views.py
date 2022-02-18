from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from FinalCoder.forms import UserRegisterForm, UserEditForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from AppFinalCoder.models import Avatar

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contrasena = form.cleaned_data['password']
            user = authenticate(username=usuario, password=contrasena)
            if user is not None:
                login (request,user)
                return redirect('inicio')
            else:
                return render (request, 'login.html',
                    {'form' : form, 'error':'Usuario y Contraseña NO VALIDOS' })        
                
        else:
            return render(request, 'login.html', {'form' : form })
    else:
        form = AuthenticationForm
        return render(request, 'login.html', {'form' : form })
    
# def register (request):
#     if request.method =='POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             form.save()
#             return HttpResponse (f'Usuario {username} fue creado correctamente')
#     else:
#         form = UserRegisterForm()
    
#     return render (request, 'registro.html', {'form':form})

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
            usuario.set_password(data['password1'])
            usuario.save()
            return redirect ('login')
    else:
        form=UserEditForm({'email':usuario.email}) 
    # return redirect ('inicio')    
    return render (request, 'registro.html',{'form':form})

def mensaje(request):
    return render(request,'mensaje.html')

@login_required
def AcercaDe(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url= avatares.last().imagen.url
    else:
        avatar_url ='ninguna'
        
    return render(request,'AcercaDe.html',{'avatar_url':avatar_url})