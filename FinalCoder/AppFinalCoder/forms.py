from django.forms import Form
from django.forms import CharField, EmailField, DateTimeField, IntegerField, FloatField

class proveedorForm(Form):
    nombre=CharField()
    domicilio= CharField()
    email = EmailField()

class clienteForm(Form):
    nombre = CharField()
    apellido = CharField()
    nacimiento = DateTimeField()
    email = EmailField()
    
class productosForm(Form):
    nombre=CharField()
    descripcion= CharField()
    cantidad= IntegerField()
    precio = FloatField()    