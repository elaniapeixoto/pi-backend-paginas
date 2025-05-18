from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def agendamento(request):
    return render(request, "agendamento.html")


def cadastro(request):
    return render(request, "cadastro.html")


def procedimento(request):
    return render(request, "procedimento.html")


def cadastro_fornecedor(request):
    return render(request, "cadastro_fornecedor.html")


def cadastro_fornecedor(request):
    estados = [
        "AC",
        "AL",
        "AP",
        "AM",
        "BA",
        "CE",
        "DF",
        "ES",
        "GO",
        "MA",
        "MT",
        "MS",
        "MG",
        "PA",
        "PB",
        "PR",
        "PE",
        "PI",
        "RJ",
        "RN",
        "RS",
        "RO",
        "RR",
        "SC",
        "SP",
        "SE",
        "TO",
    ]
    context = {
        "estados": estados,
    }
    return render(request, "cadastro_fornecedor.html", context)
