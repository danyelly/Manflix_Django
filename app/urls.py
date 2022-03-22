"""django_rest URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path("usuarios/",UsuariosAPIView.as_view(), name='usuarios'),
    path("usuarios/<int:pk>", UsuariosAPIView.as_view(), name='usuarios'),
    path("categoria/",CategoriaAPIView.as_view(), name='categoria'),
    path("categoria/<int:pk>",CategoriaAPIView.as_view(), name='categoria'),
    path("filmes/",FilmesAPIView.as_view(), name='filmes'),
    path("filmes/<int:pk>",FilmesAPIView.as_view(), name='filmes'),
    path("assinatura/",AssinaturaAPIView.as_view(), name='assinatura'),
    path("assinatura/<int:pk>",AssinaturaAPIView.as_view(), name='assinatura'),
    path("favoritos/",FavoritosAPIView.as_view(), name='favoritos'),
    path("favoritos/<int:pk>",FavoritosAPIView.as_view(), name='favoritos'),
]
