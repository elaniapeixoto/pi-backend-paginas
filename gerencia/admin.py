from django.contrib import admin
from .models import Cliente, Funcionario, Procedimento, Agendamento

admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Procedimento)
admin.site.register(Agendamento)
