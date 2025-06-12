from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *

estados = {
        "AC": "Acre",
        "AL": "Alagoas",
        "AP": "Amapá",
        "AM": "Amazonas",
        "BA": "Bahia",
        "CE": "Ceará",
        "DF": "Distrito Federal",
        "ES": "Espírito Santo",
        "GO": "Goiás",
        "MA": "Maranhão",
        "MT": "Mato Grosso",
        "MS": "Mato Grosso do Sul",
        "MG": "Minas Gerais",
        "PA": "Pará",
        "PB": "Paraíba",
        "PR": "Paraná",
        "PE": "Pernambuco",
        "PI": "Piauí",
        "RJ": "Rio de Janeiro",
        "RN": "Rio Grande do Norte",
        "RS": "Rio Grande do Sul",
        "RO": "Rondônia",
        "RR": "Roraima",
        "SC": "Santa Catarina",
        "SP": "São Paulo",
        "SE": "Sergipe",
        "TO": "Tocantins"
    }

@login_required
def index (request):
    return render(request, 'gerencia/index.html')

@login_required
def lista_pessoa(request):
    pessoas = Pessoa.objects.all()
    context = {
        "pessoas": pessoas,
    }
    return render(request, 'lista_pessoa.html', context)

@login_required
def cadastro_pessoa(request):
    return render(request, "cadastro_pessoa.html", {"estados": estados})

# @login_required
# def cadastro_usuario(request):
#     context = {
#         "estados": estados,
#     }
#     return render(request, "usuario/cadastro_usuario.html", context)

@login_required
def cadastro_agendamento(request):
    return render(request, "agendamento.html")

@login_required
def cadastro_procedimento(request):
    return render(request, "index.html")
