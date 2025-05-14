from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'principal'),
    path('agendamento', views.agendamento, name = 'agendamento'),
    path('cadastro', views.cadastro, name = 'cadastro'),
]
