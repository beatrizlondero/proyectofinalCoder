from datetime import date
from xmlrpc.client import DateTime
from django.db import models
from django.db.models import Model
from django.db.models.fields import *

class Cliente (Model):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    nacimiento = DateTime()
    email = EmailField()
    
class Proveedor(Model):
    nombre=CharField(max_length=50)
    domicilio= CharField(max_length=40)
    email = EmailField()
    
class Productos(Model):
    nombre=CharField(max_length=15)
    descripcion= CharField(max_length=50)
    cantidad= IntegerField()
    precio = FloatField()
                 
