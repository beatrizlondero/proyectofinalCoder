from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse

from AppFinalCoder.models import Proveedor
# from .models import Curso, Profesor
# from AppCoder.forms import CursoForm , ProfesorForm
def inicio (request):
    return render(request,'padre.html')
    # return HttpResponse("Incio")

def proveedores(request):
    return render(request, 'padre.html', {'Proveedor' :Proveedor.objects.all()})

def proveedoresList(request):
    return render(request, 'proveedor.html', {'Proveedor' :Proveedor.objects.all()})