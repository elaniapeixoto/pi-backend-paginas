from django.contrib import admin
from .models import Agendamento, Funcionario, Locador, MovimentoCaixa, Pessoa, Procedimento

admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Locador)
admin.site.register(Procedimento)
admin.site.register(Agendamento)
admin.site.register(MovimentoCaixa)
