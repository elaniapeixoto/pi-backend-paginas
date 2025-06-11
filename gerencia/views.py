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

def index (request):
    return render(request, 'index.html')

def lista_cliente(request):
    clientes = Cliente.objects.all()
    context = {
        "clientes": clientes,
    }
    return render(request, 'cliente/lista_cliente.html', context)

def cadastro_cliente(request):
    from .forms import ClienteForm
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "cliente/cadastro_cliente.html", {"form": ClienteForm(), "estados": estados, "success": True})
    else:
        form = ClienteForm()
    return render(request, "cliente/cadastro_cliente.html", {"form": form, "estados": estados})

def cadastro_usuario(request):
    
    context = {
        "estados": estados,
    }
    return render(request, "usuario/cadastro_usuario.html", context)

def cadastro_agendamento(request):
    return render(request, "agendamento/agendamento.html")

def cadastro_procedimento(request):
    return render(request, "index.html")
