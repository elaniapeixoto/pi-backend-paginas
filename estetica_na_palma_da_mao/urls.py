from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path("cadastro_agendamento/", views.agendamento, name="agendamento"),
    path("cadastro_pessoa/", views.cadastro_pessoa, name="cadastro_pessoa"),
    path("cadastro_procedimento/", views.procedimento, name="procedimento"),
    path("cadastro_fornecedor/", views.cadastro_fornecedor, name="cadastro_fornecedor"),
    path('login/', views.login, name='login'),
]