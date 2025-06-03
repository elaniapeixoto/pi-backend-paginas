from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    
    path('login/', views.login, name='login'),
    
    path('cadastros/', include('cadastros.urls')),

]