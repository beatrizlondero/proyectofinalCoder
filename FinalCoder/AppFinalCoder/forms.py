from django import forms
from django.forms import Form, ImageField
from django.forms import CharField, EmailField, DateField,IntegerField, FloatField
from django import forms
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
    imagen=ImageField(required=False) 
    
class AvatarFormulario(Form):
    imagen=ImageField(required=True)
    
class ComentarioFormulario(Form):
    comentario = CharField(widget= forms.Textarea)
    # fecha = DateField()