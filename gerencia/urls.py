from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("pessoa/lista/", views.lista_pessoa, name="lista_pessoa"),
    path("pessoa/cadastro/", views.cadastro_pessoa, name="cadastro_pessoa"),
    path("pessoa/editar/<int:id>/", views.editar_pessoa, name="editar_pessoa"),
    path("pessoa/deletar/<int:id>/", views.deletar_pessoa, name="deletar_pessoa"),
    path("funcionario/lista/", views.lista_funcionario, name="lista_funcionario"),
    path("funcionario/cadastro/", views.cadastro_funcionario, name="cadastro_funcionario"),
    path(
        "funcionario/editar/<int:id>/",
        views.editar_funcionario,
        name="editar_funcionario",
    ),
    path(
        "funcionario/deletar/<int:id>/",
        views.deletar_funcionario,
        name="deletar_funcionario",
    ),
    path("locador/lista/", views.lista_locador, name="lista_locador"),
    path("locador/cadastro/", views.cadastro_locador, name="cadastro_locador"),
    path("locador/editar/<int:id>/", views.cadastro_locador, name="editar_locador"),
    path("locador/deletar/<int:id>/", views.deletar_locador, name="deletar_locador"),
    path("agendamento/lista/", views.lista_agendamento, name="lista_agendamento"),
    path("agendamento/cadastro/", views.cadastro_agendamento, name="cadastro_agendamento"),
    path(
        "agendamento/editar/<int:id>/",
        views.cadastro_agendamento,
        name="editar_agendamento",
    ),
    path(
        "agendamento/deletar/<int:id>/",
        views.deletar_agendamento,
        name="deletar_agendamento",
    ),
    path("procedimentos/", views.lista_procedimento, name="lista_procedimentos"),
    path(
        "procedimentos/cadastro/",
        views.cadastro_procedimento,
        name="cadastro_procedimento",
    ),
    path(
        "procedimentos/editar/<int:id>/",
        views.cadastro_procedimento,
        name="editar_procedimento",
    ),
    path(
        "procedimentos/deletar/<int:id>/",
        views.deletar_procedimento,
        name="deletar_procedimento",
    ),
    path("caixa/lista/", views.lista_caixa, name="lista_caixa"),
    path("caixa/cadastro/", views.cadastro_caixa, name="cadastro_caixa"),
    path("caixa/editar/<int:id>/", views.cadastro_caixa, name="editar_caixa"),
    path("caixa/deletar/<int:id>/", views.deletar_caixa, name="deletar_caixa"),
    path("usuario/lista/", views.lista_usuario, name="lista_usuario"),
    path("usuario/cadastro/", views.cadastro_usuario, name="cadastro_usuario"),
]
