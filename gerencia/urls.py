from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("visitante/", include("visitante.urls"), name="visitante"),

    path("pessoa/lista/", views.lista_pessoa, name="lista_pessoa"),
    path("pessoa/cadastro/", views.cadastro_pessoa, name="cadastro_pessoa"),
    path("pessoa/editar/<int:id>/", views.editar_pessoa, name="editar_pessoa"),
    path("pessoa/deletar/<int:id>/", views.deletar_pessoa, name="deletar_pessoa"),

    path("funcionario/lista/", views.lista_funcionario, name="lista_funcionario"),
    path( "funcionario/cadastro/", views.cadastro_funcionario, name="cadastro_funcionario"),
    path("funcionario/editar/<int:id>/", views.editar_funcionario, name="editar_funcionario"),
    path("funcionario/deletar/<int:id>/", views.deletar_funcionario, name="deletar_funcionario"),

    path("agendamento/", views.cadastro_agendamento, name="cadastro_agendamento"),

    path("procedimentos/", views.lista_procedimento, name="lista_procedimentos"),
    path("procedimentos/cadastro/", views.cadastro_procedimento, name="cadastro_procedimento"),
    path("procedimentos/editar/<int:id>/",views.editar_procedimento, name="editar_procedimento"),

    path("usuario/lista/", views.lista_usuario, name="lista_usuario"),
    path("usuario/cadastro/", views.cadastro_usuario, name="cadastro_usuario"),
]
