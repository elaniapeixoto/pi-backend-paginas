from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='gerencia'),
    path("cliente/cadastro/", views.cadastro_cliente, name="cadastro_cliente"),
    path("cliente/lista/", views.lista_cliente, name="lista_cliente"),
    path("agendamento/", views.cadastro_agendamento, name="cadastro_agendamento"),
    path("procedimento/", views.cadastro_procedimento, name="cadastro_procedimento"),
]