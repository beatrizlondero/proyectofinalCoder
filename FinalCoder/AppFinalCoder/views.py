from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Curso, Profesor
# from AppCoder.forms import CursoForm , ProfesorForm
def inicio (request):
    return render(request,'padre.html')
    # return HttpResponse("Incio")

