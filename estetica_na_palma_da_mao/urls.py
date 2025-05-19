<<<<<<< Updated upstream
=======
<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path("agendamento", views.agendamento, name="agendamento"),
    path("cadastro_pessoa", views.cadastro_pessoa, name="cadastro_pessoa"),
    path("procedimento", views.procedimento, name="procedimento"),
    path("fornecedor/cadastro/", views.cadastro_fornecedor, name="cadastro_fornecedor"),
    path('login/', views.login, name='login'),
]
=======
>>>>>>> Stashed changes
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
]
<<<<<<< Updated upstream
=======
>>>>>>> 54b7b7424b2c9e3e572bdf60713a6c45b6bcda5a
>>>>>>> Stashed changes
