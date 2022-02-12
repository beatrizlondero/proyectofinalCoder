from xml.etree.ElementInclude import include
from django.urls import path
from AppFinalCoder.views import comentarios, proveedores, clientes, productos 
from django.urls import path
from AppFinalCoder.views import proveedorListView, proveedorCreateView , proveedorUpdateView, proveedoresModif
from AppFinalCoder.views import proveedorDeleteView, proveedoresBorrar
from AppFinalCoder.views import clienteListView, clienteCreateView, clienteUpdateView
from AppFinalCoder.views import clienteDeleteView, clientesBorrar, clientesModif, productoCreateView
from AppFinalCoder.views import productoListView
from AppFinalCoder.views import productosBorrar, productoDeleteView, productosModif, productoUpdateView
from AppFinalCoder.views import agregar_comentario
urlpatterns = [
    # path('', inicio, name="Inicio"),
    path('proveedores/list', proveedorListView.as_view(), name="proveedoresList"),
    path('proveedores/add', proveedorCreateView.as_view(), name="proveedoresAdd"),
    path('proveedores/', proveedores , name="proveedores"),
    path('proveedores/modificar/<pk>', proveedorUpdateView.as_view(), name="proveedoresUpdate"),
    path('proveedores/modif>',proveedoresModif.as_view() , name="proveedoresModif"),
    path('proveedores/borrar>',proveedoresBorrar.as_view() , name="proveedoresBorrar"),
    path('proveedores/del/<pk>', proveedorDeleteView.as_view(), name="proveedoresDel"),
    path('clientes/list', clienteListView.as_view(), name="clientesList"),
    path('clientes/add', clienteCreateView.as_view(), name="clientesAdd"),
    path('clientes/', clientes , name="clientes"),
    path('clientes/modificar/<pk>', clienteUpdateView.as_view(), name="clientesUpdate"),
    path('clientes/modif>',clientesModif.as_view() , name="clientesModif"),
    path('clientes/borrar>',clientesBorrar.as_view() , name="clientesBorrar"),
    path('clientes/del/<pk>', clienteDeleteView.as_view(), name="clientesDel"),
    path('productos/add', productoCreateView.as_view(), name="productosAdd"),
    path('productos/', productos , name="productos"),
    path('productos/list', productoListView.as_view() , name="productosList"),
    path('productos/borrar', productosBorrar.as_view() , name="productosBorrar"),
    path('productos/modif>',productosModif.as_view() , name="productosModif"),
    path('productos/modificar/<pk>', productoUpdateView.as_view(), name="productosUpdate"),
    path('productos/del/<pk>', productoDeleteView.as_view(), name="productosDel"),
    
    path('comentarios/', comentarios , name="comentarios"),
    path('comentarios/add', agregar_comentario , name="comentariosAdd"),
    # path('comentarios/del', productosBorrar.as_view() , name="comentariosDel"),
    # path('comentarios/find', productosBorrar.as_view() , name="comentariosFind"),
]
