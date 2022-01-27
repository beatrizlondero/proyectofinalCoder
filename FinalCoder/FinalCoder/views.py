from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from FinalCoder.forms import UserRegisterForm

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
def mensaje(request):
    return render(request,'mensaje.html')