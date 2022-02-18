"""FinalCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from AppFinalCoder.views import agregar_avatar
from FinalCoder.views import editar_perfil, AcercaDe
from FinalCoder.views import UserCreateView
from FinalCoder.views import login_request, mensaje
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AcercaDe , name="inicio"),
    path('finalcoder', include("AppFinalCoder.urls")),
    path('login',login_request,name = 'login'),
    path('register', UserCreateView.as_view(), name='register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('mensaje', mensaje, name='mensaje'),
    path('editarperfil',editar_perfil, name='editarperfil'),
    path('agregaravatar',agregar_avatar, name='agregaravatar'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
