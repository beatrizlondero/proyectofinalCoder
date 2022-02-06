from django.forms import Form, ImageField
from django.forms import CharField, EmailField, DateField, IntegerField, FloatField

class proveedorForm(Form):
    nombre=CharField()
    domicilio= CharField()
    email = EmailField()

class clienteForm(Form):
    nombre = CharField()
    apellido = CharField()
    nacimiento = DateField(input_formats=['%m %d %Y'])
    email = EmailField()
    
class productosForm(Form):
    nombre=CharField()
    descripcion= CharField()
    cantidad= IntegerField()
    precio = FloatField()    
    
class AvatarFomrulario(Form):
    imagen=ImageField(required=True)