from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="principal"),
    path("agendamento", views.agendamento, name="agendamento"),
    path("cadastro", views.cadastro, name="cadastro"),
    path("procedimento", views.procedimento, name="procedimento"),
    path("fornecedor/cadastro/", views.cadastro_fornecedor, name="cadastro_fornecedor"),
    path('login/', views.login, name='login'),
    path('menu/', views.menu, name='menu'),
]