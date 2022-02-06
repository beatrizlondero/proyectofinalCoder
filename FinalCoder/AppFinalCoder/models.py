from distutils.command.upload import upload
from django.db import models
from django.db.models import Model , ForeignKey, CASCADE , ImageField
from django.db.models.fields import CharField, EmailField, DateField, IntegerField, FloatField
from django.contrib.auth.models import User

class Avatar(Model):
    user= ForeignKey (User, on_delete=CASCADE)
    imagen = ImageField (upload_to = 'avatares', null = True, blank=True)
    
class Cliente (Model):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    nacimiento = DateField()
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
