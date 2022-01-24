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
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Fecha de Nacimiento {self.nacimiento} - Email: {self.email}"

    
class Proveedor(Model):
    nombre=CharField(max_length=50)
    domicilio= CharField(max_length=40)
    email = EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Domicilio: {self.domicilio} - Email: {self.email}"

class Productos(Model):
    nombre=CharField(max_length=15)
    descripcion= CharField(max_length=50)
    cantidad= IntegerField()
    precio = FloatField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Descripción: {self.descripcion} - Cantidad {self.cantidad} - Precio: {self.precio}"             
