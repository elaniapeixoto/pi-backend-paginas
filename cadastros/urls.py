from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("agendamento/", views.agendamento, name="agendamento"),
    path("pessoa/", views.cadastro_pessoa, name="cadastro_pessoa"),
    path("procedimento/", views.cadastro_procedimento, name="cadastro_procedimento"),
    path("fornecedor/", views.cadastro_fornecedor, name="cadastro_fornecedor"),

]