from xml.etree.ElementInclude import include
from django.urls import path
from AppFinalCoder.views import inicio, proveedores
from django.urls import path
from AppFinalCoder.views import proveedorListView, proveedorCreateView , proveedorUpdateView, proveedoresModif
from AppFinalCoder.views import proveedorDeleteView, proveedoresBorrar
urlpatterns = [
    path('', inicio, name="Inicio"),
    path('proveedores/list', proveedorListView.as_view(), name="proveedoresList"),
    path('proveedores/add', proveedorCreateView.as_view(), name="proveedoresAdd"),
    path('proveedores/', proveedores , name="proveedores"),
    path('proveedores/modificar/<pk>', proveedorUpdateView.as_view(), name="proveedoresUpdate"),
    path('proveedores/modif>',proveedoresModif.as_view() , name="proveedoresModif"),
    path('proveedores/borrar>',proveedoresBorrar.as_view() , name="proveedoresBorrar"),
    path('proveedores/del/<pk>', proveedorDeleteView.as_view(), name="proveedoresDel"),
]
