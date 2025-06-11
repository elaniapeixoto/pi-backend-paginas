from django.contrib import admin

from .models import *


class ClienteAdmin(admin.ModelAdmin):
    fields = ['nome', 'cpf', 'numero', 'data_nascimento','email', 'cep', 'rua', 'cidade', 'estado', 'tipo', 'observacoes']

    list_display = ['nome', 'cpf', 'numero', 'data_nascimento','email', 'cep', 'rua', 'cidade', 'estado', 'tipo', 'observacoes']
    list_filter = ['nome', 'cpf', 'numero', 'data_nascimento','email', 'cep', 'rua', 'cidade', 'estado', 'tipo', 'observacoes']
    ordering= ['nome']
    search_fields = ['nome', 'cpf', 'numero']
    actions_on_bottom = True
    
admin.site.register(Cliente, ClienteAdmin)  
admin.site.register(Funcionario)  
admin.site.register(Locador)  
admin.site.register(Procedimento)  
admin.site.register(Agendamento)  
