from django.contrib import admin
from .models import Pessoa, Funcionario, Procedimento, Agendamento

admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Procedimento)
admin.site.register(Agendamento)
