"""Veterinaria_Luna URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Sistema_Veterinario import views

urlpatterns = [
    #Parte del Login
    path("", views.loginDef, name="login"),
    path("loginV/", views.loginV, name="loginV"),
    path("registrate/", views.registrarseDef, name="registrarse"),
    path("registrateV/", views.registrarseV, name="registrarseV"),
    path("menu/", views.menuDef, name="menu"),

    #Parte del Cliente
    path("generalC/", views.clientesDef, name="generalC1"),
    path("generalCBuscar/", views.buscarCliente, name="generalC2"),
    path('generalC/registrarCliente/', views.crearCliente, name="registrarC1"),
    path('generalC/registrarC/', views.registrarCliente, name="registrarC2"),
    path('generalC/edicionCliente/<id>', views.edicionCliente, name="edicionC1"),
    path('generalC/editarCliente/', views.editarCliente, name="edicionC2"),
    path('generalC/eliminarCliente/<id>', views.eliminarCliente, name="eliminarC"),

    #Parte de la Mascota
    path("generalM/", views.mascotasDef, name="generalM1"),
    path("generalMBuscar/", views.buscarMascota, name="generalM2"),
    path('generalM/registrarMascota/', views.crearMascota, name="registrarM1"),
    path('generalM/registrarM/', views.registrarMascota, name="registrarM2"),
    path('generalM/edicionMascota/<id>', views.edicionMascota, name="edicionM1"),
    path('generalM/editarMascota/', views.editarMascota, name="edicionM2"),
    path('generalM/eliminarMascota/<id>', views.eliminarMascota, name="eliminarM"),

    # Parte de la Agenda Cita
    path("generalAC/", views.agendaCitaDef, name="generalAC1"),
    path("generalACBuscar/", views.buscarCita, name="generalAC2"),
    path('generalAC/registrarACitas/', views.crearCita, name="registrarAC1"),
    path('generalAC/registrarAC/', views.registrarCitas, name="registrarAC2"),
    path('generalAC/edicionACitas/<id>', views.edicionCita, name="edicionAC1"),
    path('generalAC/editarACitas/', views.editarCita, name="edicionAC2"),
    path('generalAC/eliminarACitas/<id>', views.eliminarCita, name="eliminarAC"),
]
