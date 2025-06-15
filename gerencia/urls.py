from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('visitante/', include('visitante.urls'), name='visitante'),
    
    
    # PESSOAS
    path("pessoa/lista/", views.lista_pessoa, name="lista_pessoa"),
    path("pessoa/cadastro/", views.cadastro_pessoa, name="cadastro_pessoa"),
    path("pessoa/editar/<int:id>/", views.editar_pessoa, name="editar_pessoa"),

    # FUNCIONARIO
    path("funcionario/lista/", views.lista_funcionario, name="lista_funcionario"),
    path("funcionario/cadastro/", views.cadastro_funcionario, name="cadastro_funcionario"),
    path("funcionario/editar/<int:id>/", views.editar_funcionario, name="editar_funcionario"),
    
    # AGENDA
    path("agendamento/", views.cadastro_agendamento, name="cadastro_agendamento"),
    
    # SERVICOS
    path("procedimento/", views.cadastro_procedimento, name="cadastro_procedimento"),

    #FUNCIONÁRIOS
    path("funcionario/lista/", views.lista_funcionario, name="lista_funcionario"),
    path("funcionario/cadastro/", views.cadastro_funcionario, name="cadastro_funcionario"),
    path("funcionario/editar/<int:id>/", views.editar_funcionario, name="editar_funcionario"),
]