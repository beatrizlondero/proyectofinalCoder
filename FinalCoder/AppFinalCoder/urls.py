from xml.etree.ElementInclude import include
from django.urls import path
from AppFinalCoder.views import inicio, proveedoresAdd, proveedoresDel, proveedores
from django.urls import path
from AppFinalCoder.views import proveedorListView
urlpatterns = [
    path('', inicio, name="Inicio"),
    path('proveedores/list', proveedorListView.as_view(), name="proveedoresList"),
    path('proveedores/add', proveedoresAdd, name="proveedoresAdd"),
    path('proveedores/', proveedores , name="proveedores"),
    path('proveedores/del/<proveedorNombre>', proveedoresDel, name="proveedoresDel"),

]
