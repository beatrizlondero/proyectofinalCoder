from xml.etree.ElementInclude import include
from django.urls import path
from AppFinalCoder.views import inicio 
from django.urls import path
urlpatterns = [
    path('', inicio, name="Inicio"),

]
